from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import re
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError


ZHOUYI_KING_WEN_ORDER = [
    "乾", "坤", "屯", "蒙", "需", "訟", "師", "比", "小畜", "履",
    "泰", "否", "同人", "大有", "謙", "豫", "隨", "蠱", "臨", "觀",
    "噬嗑", "賁", "剝", "復", "无妄", "大畜", "頤", "大過", "坎", "離",
    "咸", "恒", "遯", "大壯", "晉", "明夷", "家人", "睽", "蹇", "解",
    "損", "益", "夬", "姤", "萃", "升", "困", "井", "革", "鼎",
    "震", "艮", "漸", "歸妹", "豐", "旅", "巽", "兌", "渙", "節",
    "中孚", "小過", "既濟", "未濟",
]
ZHOUYI_APPENDIX_ORDER = [
    "彖", "大象", "小象", "文言", "繫辭上", "繫辭下", "說卦", "序卦", "雜卦",
]
ZHOUYI_NAME_INDEX = {
    name: index for index, name in enumerate(ZHOUYI_KING_WEN_ORDER, start=1)
}
ZHOUYI_NAME_INDEX.update({"無妄": ZHOUYI_NAME_INDEX["无妄"], "恆": ZHOUYI_NAME_INDEX["恒"]})


def api_json(api_base: str, params: dict[str, str]) -> dict[str, Any]:
    url = f"{api_base}?{urllib.parse.urlencode(params)}"
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "personal-wisdom-skills/1.0 (educational source archiver)",
        },
    )
    for attempt in range(5):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.loads(response.read().decode("utf-8"))
        except HTTPError as error:
            if error.code != 429 or attempt == 4:
                raise
            retry_after = error.headers.get("Retry-After")
            delay = float(retry_after) if retry_after else float(2**attempt)
            time.sleep(delay)

    raise RuntimeError("unreachable")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def wikisource_page_key(title: str, root_title: str) -> tuple[int, int, int, str]:
    """Sort numeric Wikisource subpages in reading order, not lexically."""
    if title == root_title:
        return (0, 0, 0, "")
    suffix = title.removeprefix(f"{root_title}/")
    if suffix == "序":
        return (1, 0, 0, "")
    match = re.fullmatch(r"(\d+)(又(\d*)?)?(?:/(.*))?", suffix)
    if not match:
        return (3, 0, 0, suffix)
    chapter = int(match.group(1))
    repeated = match.group(2) is not None
    repeat_number = int(match.group(3) or 1) if repeated else 0
    nested = match.group(4) or ""
    variant = 2 + repeat_number if repeated else (1 if nested else 0)
    return (2, chapter, variant, nested)


def order_wikisource_pages(root_title: str, subpages: list[str]) -> list[str]:
    if root_title == "周易正義":
        def zhengyi_key(page: str) -> tuple[int, int, int, str]:
            suffix = page.removeprefix(f"{root_title}/")
            hexagram = re.fullmatch(r"(\d{2})([^\d.].*)", suffix)
            if hexagram:
                volume = int(hexagram.group(1))
                name = hexagram.group(2)
                return (volume, 0, ZHOUYI_NAME_INDEX.get(name, 999), name)
            section = re.fullmatch(r"(\d+)[.](\d+)", suffix)
            if section:
                return (int(section.group(1)), 1, int(section.group(2)), "")
            volume_only = re.fullmatch(r"(\d+)", suffix)
            if volume_only:
                return (int(volume_only.group(1)), 2, 0, "")
            return (999, 9, 0, suffix)

        return [root_title] + sorted(subpages, key=zhengyi_key)

    if root_title != "周易":
        return [root_title] + sorted(
            subpages,
            key=lambda page: wikisource_page_key(page, root_title),
        )

    preferred = [
        f"{root_title}/{name}"
        for name in ZHOUYI_KING_WEN_ORDER + ZHOUYI_APPENDIX_ORDER
    ]
    available = set(subpages)
    ordered = [page for page in preferred if page in available]
    extras = sorted(available.difference(ordered))
    return [root_title, *ordered, *extras]


def fetch_github_mirror(
    source_url: str,
    source_commit: str,
    title: str,
    output_dir: Path,
    limitation: str,
) -> dict[str, object]:
    request = urllib.request.Request(
        source_url,
        headers={
            "User-Agent": "personal-wisdom-skills/1.0 (educational source archiver)",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        text = response.read().decode("utf-8")
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "raw-wikitext.txt").write_text(
        text,
        encoding="utf-8",
        newline="\n",
    )
    manifest: dict[str, object] = {
        "title": title,
        "source_type": "github-mirror",
        "source_format": "plain-text",
        "source_url": source_url,
        "source_commit": source_commit,
        "upstream_wikisource_url": (
            f"https://zh.wikisource.org/wiki/{urllib.parse.quote(title)}"
        ),
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "page_count": 1,
        "pages": [title],
        "sha256": sha256_text(text),
        "limitations": limitation,
    }
    (output_dir / "source-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return manifest


def fetch_page_wikitext(api_base: str, page: str) -> str:
    parsed = api_json(
        api_base,
        {
            "action": "parse",
            "page": page,
            "prop": "wikitext",
            "format": "json",
        },
    )
    return f"\n===== {page} =====\n{parsed['parse']['wikitext']['*'].strip()}\n"


def fetch_pages_batch(
    api_base: str,
    pages: list[str],
    batch_size: int = 20,
) -> list[str]:
    if batch_size < 1 or batch_size > 50:
        raise ValueError("batch_size must be between 1 and 50")

    content_by_requested_title: dict[str, str] = {}
    for start in range(0, len(pages), batch_size):
        requested = pages[start : start + batch_size]
        payload = api_json(
            api_base,
            {
                "action": "query",
                "prop": "revisions",
                "rvprop": "content",
                "rvslots": "main",
                "titles": "|".join(requested),
                "redirects": "1",
                "format": "json",
                "formatversion": "2",
            },
        )
        query = payload["query"]
        alias_to_canonical = {
            item["from"]: item["to"]
            for key in ("normalized", "redirects")
            for item in query.get(key, [])
        }
        returned = {item["title"]: item for item in query["pages"]}
        for title in requested:
            canonical = alias_to_canonical.get(title, title)
            page = returned.get(canonical)
            if not page or page.get("missing") is True or not page.get("revisions"):
                raise RuntimeError(f"Wikisource page has no revision content: {title}")
            revision = page["revisions"][0]
            content_by_requested_title[title] = revision["slots"]["main"]["content"]

    return [
        f"\n===== {page} =====\n{content_by_requested_title[page].strip()}\n"
        for page in pages
    ]


def fetch_book(
    api_base: str,
    title: str,
    output_dir: Path,
    workers: int = 1,
    batch_size: int | None = None,
) -> dict[str, object]:
    listing = api_json(
        api_base,
        {
            "action": "query",
            "list": "allpages",
            "apprefix": f"{title}/",
            "apnamespace": "0",
            "aplimit": "max",
            "format": "json",
        },
    )
    pages = order_wikisource_pages(
        title,
        [item["title"] for item in listing["query"]["allpages"]],
    )

    if batch_size is not None:
        sections = fetch_pages_batch(api_base, pages, batch_size=batch_size)
    elif workers < 1:
        raise ValueError("workers must be at least 1")
    elif workers == 1:
        sections = [fetch_page_wikitext(api_base, page) for page in pages]
    else:
        with ThreadPoolExecutor(max_workers=workers) as executor:
            sections = list(
                executor.map(
                    lambda page: fetch_page_wikitext(api_base, page),
                    pages,
                )
            )

    combined = "".join(sections)
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "raw-wikitext.txt").write_text(
        combined,
        encoding="utf-8",
        newline="\n",
    )
    manifest: dict[str, object] = {
        "title": title,
        "source_url": f"https://zh.wikisource.org/wiki/{urllib.parse.quote(title)}",
        "api_base": api_base,
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "page_count": len(pages),
        "pages": pages,
        "order_strategy": (
            "king-wen-64-then-appendices"
            if title == "周易"
            else "volume-then-king-wen-or-section-order"
            if title == "周易正義"
            else "numeric-subpage-reading-order"
        ),
        "sha256": sha256_text(combined),
    }
    (output_dir / "source-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--title",
        default="增刪卜易",
        help="Wikisource root page title to archive (default: 增刪卜易)",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=4,
        help="Concurrent page fetches; output order remains deterministic (default: 4)",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=20,
        help="Pages per official revision API request, 1-50 (default: 20)",
    )
    parser.add_argument("--fallback-url")
    parser.add_argument("--fallback-commit")
    parser.add_argument(
        "--limitation",
        default="Wikimedia API remained rate-limited with HTTP 429.",
    )
    args = parser.parse_args()
    if bool(args.fallback_url) != bool(args.fallback_commit):
        parser.error("--fallback-url and --fallback-commit must be provided together")
    if args.fallback_url:
        manifest = fetch_github_mirror(
            args.fallback_url,
            args.fallback_commit,
            args.title,
            args.output,
            args.limitation,
        )
    else:
        manifest = fetch_book(
            "https://zh.wikisource.org/w/api.php",
            args.title,
            args.output,
            workers=args.workers,
            batch_size=args.batch_size,
        )
    print(
        json.dumps(
            manifest,
            ensure_ascii=False,
            indent=2,
        )
    )
