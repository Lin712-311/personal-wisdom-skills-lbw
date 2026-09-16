import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from urllib.error import HTTPError
from unittest.mock import MagicMock, patch

from scripts.fetch_wikisource import (
    api_json,
    fetch_book,
    fetch_github_mirror,
    fetch_pages_batch,
    order_wikisource_pages,
    sha256_text,
    wikisource_page_key,
)


class FetchWikisourceTests(unittest.TestCase):
    def test_cli_accepts_a_custom_title(self):
        completed = subprocess.run(
            [sys.executable, "scripts/fetch_wikisource.py", "--help"],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        self.assertIn("--title", completed.stdout)

    def test_sha256_is_stable(self):
        self.assertEqual(
            sha256_text("abc"),
            "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
        )

    @patch("scripts.fetch_wikisource.time.sleep")
    @patch("scripts.fetch_wikisource.urllib.request.urlopen")
    def test_api_json_retries_http_429(self, urlopen, sleep):
        response = MagicMock()
        response.__enter__.return_value.read.return_value = b'{"query": {}}'
        urlopen.side_effect = [
            HTTPError(
                "https://example.invalid/w/api.php",
                429,
                "Too Many Requests",
                {"Retry-After": "2"},
                None,
            ),
            response,
        ]

        self.assertEqual(api_json("https://example.invalid/w/api.php", {}), {"query": {}})
        sleep.assert_called_once_with(2.0)

    @patch("scripts.fetch_wikisource.api_json")
    def test_fetch_book_orders_main_page_before_subpages(self, api_json):
        api_json.side_effect = [
            {"query": {"allpages": [{"title": "增刪卜易/2"}, {"title": "增刪卜易/1"}]}},
            {"parse": {"wikitext": {"*": "MAIN"}}},
            {"parse": {"wikitext": {"*": "ONE"}}},
            {"parse": {"wikitext": {"*": "TWO"}}},
        ]
        with tempfile.TemporaryDirectory() as tmp:
            manifest = fetch_book("https://example.invalid/w/api.php", "增刪卜易", Path(tmp))
            text = (Path(tmp) / "raw-wikitext.txt").read_text(encoding="utf-8")
            self.assertLess(text.index("MAIN"), text.index("ONE"))
            self.assertLess(text.index("ONE"), text.index("TWO"))
            self.assertEqual(manifest["page_count"], 3)
            self.assertEqual(
                json.loads(
                    (Path(tmp) / "source-manifest.json").read_text(encoding="utf-8")
                )["sha256"],
                manifest["sha256"],
            )

    def test_wikisource_page_key_uses_reading_order(self):
        pages = [
            "增刪卜易/10",
            "增刪卜易/3/八卦各宮全圖",
            "增刪卜易/2",
            "增刪卜易/26又2",
            "增刪卜易/序",
            "增刪卜易/26",
            "增刪卜易/26又1",
            "增刪卜易/3",
        ]
        self.assertEqual(
            sorted(pages, key=lambda page: wikisource_page_key(page, "增刪卜易")),
            [
                "增刪卜易/序",
                "增刪卜易/2",
                "增刪卜易/3",
                "增刪卜易/3/八卦各宮全圖",
                "增刪卜易/10",
                "增刪卜易/26",
                "增刪卜易/26又1",
                "增刪卜易/26又2",
            ],
        )

    def test_zhouyi_pages_use_king_wen_order_then_appendices(self):
        pages = [
            "周易/雜卦",
            "周易/未濟",
            "周易/乾",
            "周易/坤",
            "周易/繫辭上",
            "周易/屯",
        ]

        self.assertEqual(
            order_wikisource_pages("周易", pages),
            [
                "周易",
                "周易/乾",
                "周易/坤",
                "周易/屯",
                "周易/未濟",
                "周易/繫辭上",
                "周易/雜卦",
            ],
        )

    def test_zhouyi_zhengyi_pages_use_volume_and_hexagram_order(self):
        pages = [
            "周易正義/10",
            "周易正義/02否",
            "周易正義/01蒙",
            "周易正義/07.10",
            "周易正義/02泰",
            "周易正義/01乾",
            "周易正義/07.02",
        ]

        self.assertEqual(
            order_wikisource_pages("周易正義", pages),
            [
                "周易正義",
                "周易正義/01乾",
                "周易正義/01蒙",
                "周易正義/02泰",
                "周易正義/02否",
                "周易正義/07.02",
                "周易正義/07.10",
                "周易正義/10",
            ],
        )

    @patch("scripts.fetch_wikisource.api_json")
    def test_fetch_book_succeeds_when_allpages_is_empty(self, api_json):
        api_json.side_effect = [
            {"query": {"allpages": []}},
            {"parse": {"wikitext": {"*": "COMPLETE MAIN PAGE"}}},
        ]
        with tempfile.TemporaryDirectory() as tmp:
            manifest = fetch_book("https://example.invalid/w/api.php", "增刪卜易", Path(tmp))
            text = (Path(tmp) / "raw-wikitext.txt").read_text(encoding="utf-8")

            self.assertIn("COMPLETE MAIN PAGE", text)
            self.assertEqual(manifest["page_count"], 1)
            self.assertEqual(manifest["pages"], ["增刪卜易"])
            self.assertEqual(manifest["sha256"], sha256_text(text))

    @patch("scripts.fetch_wikisource.fetch_page_wikitext")
    @patch("scripts.fetch_wikisource.api_json")
    def test_parallel_fetch_preserves_page_order(self, api_json, fetch_page):
        api_json.return_value = {
            "query": {"allpages": [{"title": "示例/2"}, {"title": "示例/1"}]}
        }
        fetch_page.side_effect = lambda _api, page: f"\n===== {page} =====\n{page}\n"
        with tempfile.TemporaryDirectory() as tmp:
            manifest = fetch_book(
                "https://example.invalid/w/api.php",
                "示例",
                Path(tmp),
                workers=2,
            )
            text = (Path(tmp) / "raw-wikitext.txt").read_text(encoding="utf-8")

            self.assertLess(text.index("===== 示例 ====="), text.index("===== 示例/1 ====="))
            self.assertLess(text.index("===== 示例/1 ====="), text.index("===== 示例/2 ====="))
            self.assertEqual(manifest["pages"], ["示例", "示例/1", "示例/2"])

    @patch("scripts.fetch_wikisource.api_json")
    def test_batch_fetch_resolves_redirect_and_preserves_requested_heading(self, api_json):
        api_json.return_value = {
            "query": {
                "redirects": [{"from": "周易", "to": "易經"}],
                "pages": [
                    {
                        "title": "易經",
                        "revisions": [{"slots": {"main": {"content": "CORE"}}}],
                    },
                    {
                        "title": "周易/乾",
                        "revisions": [{"slots": {"main": {"content": "QIAN"}}}],
                    },
                ],
            }
        }

        sections = fetch_pages_batch(
            "https://example.invalid/w/api.php",
            ["周易", "周易/乾"],
            batch_size=20,
        )

        self.assertEqual(sections[0], "\n===== 周易 =====\nCORE\n")
        self.assertEqual(sections[1], "\n===== 周易/乾 =====\nQIAN\n")

    @patch("scripts.fetch_wikisource.urllib.request.urlopen")
    def test_github_fallback_records_mirror_and_limitation(self, urlopen):
        response = MagicMock()
        response.__enter__.return_value.read.return_value = "完整文本\n".encode("utf-8")
        urlopen.return_value = response
        with tempfile.TemporaryDirectory() as tmp:
            manifest = fetch_github_mirror(
                "https://raw.githubusercontent.com/example/repo/abc123/book.txt",
                "abc123",
                "增刪卜易",
                Path(tmp),
                "Wikimedia API remained rate-limited with HTTP 429.",
            )

            self.assertEqual(manifest["page_count"], 1)
            self.assertEqual(manifest["source_type"], "github-mirror")
            self.assertEqual(manifest["source_commit"], "abc123")
            self.assertIn("rate-limited", manifest["limitations"])
            self.assertEqual(
                manifest["sha256"],
                sha256_text("完整文本\n"),
            )

if __name__ == "__main__":
    unittest.main()
