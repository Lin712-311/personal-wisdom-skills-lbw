"""Build a deterministic Najia Liuyao chart from six coin-line values."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from hexagrams import derive


ENGINE_COMMIT = "53291663a4c733c4cbdfa174a8d3075475c07fd3"
KNOWN_CATEGORIES = (
    "事业",
    "考试",
    "姻缘",
    "财运",
    "健康",
    "出行",
    "失物",
    "求子",
    "官非",
    "搬迁",
    "合作",
    "寻物",
    "方案占",
    "谋望",
)


def values_to_engine(values: list[int]) -> tuple[str, dict[int, str]]:
    """Convert bottom-to-top 6/7/8/9 values to engine bits and moving lines."""
    if len(values) != 6:
        raise ValueError(f"expected exactly six line values, got {len(values)}")
    if any(type(value) is not int or value not in (6, 7, 8, 9) for value in values):
        raise ValueError("each line value must be one of 6, 7, 8, or 9")

    bits = "".join("1" if value in (7, 9) else "0" for value in values)
    moving = {
        position: "老阴" if value == 6 else "老阳"
        for position, value in enumerate(values, start=1)
        if value in (6, 9)
    }
    return bits, moving


def localize_cast_time(cast_time: str, timezone_name: str) -> datetime:
    """Interpret an ISO timestamp in an IANA zone and return its local wall time."""
    try:
        timezone = ZoneInfo(timezone_name)
    except ZoneInfoNotFoundError as error:
        raise ValueError(f"unknown IANA timezone: {timezone_name}") from error

    try:
        parsed = datetime.fromisoformat(cast_time)
    except ValueError as error:
        raise ValueError("cast time must be ISO 8601, e.g. 2026-09-17T15:42:00") from error

    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone)
    return parsed.astimezone(timezone)


def build_chart(
    values: list[int],
    *,
    cast_time: str,
    timezone_name: str,
    category: str,
    question: str,
) -> dict[str, object]:
    """Return a reproducible basic chart plus deterministic Najia fields."""
    try:
        from liuyao import build_reading, compute_four_pillars
    except ImportError as error:
        raise RuntimeError(
            "liuyao-engine is not installed; install requirements-liuyao.txt first"
        ) from error

    if category not in KNOWN_CATEGORIES:
        raise ValueError(f"unsupported category: {category}")

    bits, moving = values_to_engine(values)
    local_time = localize_cast_time(cast_time, timezone_name)
    offset = local_time.utcoffset()
    if offset is None:
        raise ValueError("timezone offset could not be determined")
    offset_minutes = int(offset.total_seconds() // 60)

    pillars = compute_four_pillars(
        local_time.year,
        local_time.month,
        local_time.day,
        local_time.hour,
        local_time.minute,
        tz_offset_minutes=offset_minutes,
    )
    reading = build_reading(
        category=category,
        text=question,
        bits=bits,
        moving=moving,
        four_pillars=pillars,
    )
    reading["castTime"]["localTime"] = local_time.isoformat()
    reading["castTime"]["timezone"] = timezone_name
    reading["castTime"]["utcOffsetMinutes"] = offset_minutes

    return {
        "schemaVersion": 1,
        "engine": {
            "name": "yaomancy/liuyao-engine",
            "version": "0.1.0",
            "commit": ENGINE_COMMIT,
        },
        "input": {
            "values": values,
            "order": "初爻到上爻",
            "bits": bits,
            "moving": moving,
        },
        "hexagram": derive(values),
        "najia": reading,
        "limits": [
            "排盘字段表示所选传统规则的确定性计算，不证明现实预测效力。",
            "用神两现、伏神、规则冲突和精确应期仍须保留来源及未决项。",
            "不要把引擎 assessment 自动翻译成成功率或确定吉凶。",
        ],
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Derive a time-aware Najia Liuyao chart from six bottom-to-top values."
    )
    parser.add_argument("values", type=int, nargs=6, metavar="LINE")
    parser.add_argument("--cast-time", required=True, help="ISO 8601 local cast time")
    parser.add_argument("--timezone", required=True, help="IANA timezone, e.g. Australia/Sydney")
    parser.add_argument("--category", required=True, choices=KNOWN_CATEGORIES)
    parser.add_argument("--question", required=True)
    return parser


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    parser = build_parser()
    args = parser.parse_args()
    try:
        result = build_chart(
            args.values,
            cast_time=args.cast_time,
            timezone_name=args.timezone,
            category=args.category,
            question=args.question,
        )
    except (RuntimeError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
