from __future__ import annotations

import argparse
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


def fetch_book(api_base: str, title: str, output_dir: Path) -> dict[str, object]:
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
    pages = [title] + sorted(
        (item["title"] for item in listing["query"]["allpages"]),
        key=lambda page: wikisource_page_key(page, title),
    )

    sections: list[str] = []
    for page in pages:
        parsed = api_json(
            api_base,
            {
                "action": "parse",
                "page": page,
                "prop": "wikitext",
                "format": "json",
            },
        )
        sections.append(
            f"\n===== {page} =====\n{parsed['parse']['wikitext']['*'].strip()}\n"
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
            "增刪卜易",
            args.output,
            args.limitation,
        )
    else:
        manifest = fetch_book(
            "https://zh.wikisource.org/w/api.php",
            "增刪卜易",
            args.output,
        )
    print(
        json.dumps(
            manifest,
            ensure_ascii=False,
            indent=2,
        )
    )
