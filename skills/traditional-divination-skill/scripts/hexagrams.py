"""Deterministic six-line hexagram calculation.

Every line sequence in this module is ordered from the bottom line to the top
line (初爻到上爻). The outer key of ``KING_WEN`` is the upper trigram and the
inner key is the lower trigram.
"""

from typing import Sequence


TRIGRAMS = {
    "111": "乾",
    "110": "兑",
    "101": "离",
    "100": "震",
    "011": "巽",
    "010": "坎",
    "001": "艮",
    "000": "坤",
}

KING_WEN = {
    "乾": {"乾": 1, "兑": 10, "离": 13, "震": 25, "巽": 44, "坎": 6, "艮": 33, "坤": 12},
    "兑": {"乾": 43, "兑": 58, "离": 49, "震": 17, "巽": 28, "坎": 47, "艮": 31, "坤": 45},
    "离": {"乾": 14, "兑": 38, "离": 30, "震": 21, "巽": 50, "坎": 64, "艮": 56, "坤": 35},
    "震": {"乾": 34, "兑": 54, "离": 55, "震": 51, "巽": 32, "坎": 40, "艮": 62, "坤": 16},
    "巽": {"乾": 9, "兑": 61, "离": 37, "震": 42, "巽": 57, "坎": 59, "艮": 53, "坤": 20},
    "坎": {"乾": 5, "兑": 60, "离": 63, "震": 3, "巽": 48, "坎": 29, "艮": 39, "坤": 8},
    "艮": {"乾": 26, "兑": 41, "离": 22, "震": 27, "巽": 18, "坎": 4, "艮": 52, "坤": 23},
    "坤": {"乾": 11, "兑": 19, "离": 36, "震": 24, "巽": 46, "坎": 7, "艮": 15, "坤": 2},
}

HEXAGRAM_NAMES = {
    1: "乾", 2: "坤", 3: "屯", 4: "蒙", 5: "需", 6: "讼", 7: "师", 8: "比",
    9: "小畜", 10: "履", 11: "泰", 12: "否", 13: "同人", 14: "大有", 15: "谦", 16: "豫",
    17: "随", 18: "蛊", 19: "临", 20: "观", 21: "噬嗑", 22: "贲", 23: "剥", 24: "复",
    25: "无妄", 26: "大畜", 27: "颐", 28: "大过", 29: "坎", 30: "离", 31: "咸", 32: "恒",
    33: "遁", 34: "大壮", 35: "晋", 36: "明夷", 37: "家人", 38: "睽", 39: "蹇", 40: "解",
    41: "损", 42: "益", 43: "夬", 44: "姤", 45: "萃", 46: "升", 47: "困", 48: "井",
    49: "革", 50: "鼎", 51: "震", 52: "艮", 53: "渐", 54: "归妹", 55: "丰", 56: "旅",
    57: "巽", 58: "兑", 59: "涣", 60: "节", 61: "中孚", 62: "小过", 63: "既济", 64: "未济",
}

ORIGINAL_BIT = {6: 0, 7: 1, 8: 0, 9: 1}
CHANGED_BIT = {6: 1, 7: 1, 8: 0, 9: 0}


def _identify(bits: Sequence[int]) -> dict[str, object]:
    """Return the named hexagram represented by six bottom-to-top bits."""
    lower = TRIGRAMS["".join(str(bit) for bit in bits[:3])]
    upper = TRIGRAMS["".join(str(bit) for bit in bits[3:])]
    number = KING_WEN[upper][lower]
    return {
        "number": number,
        "name": HEXAGRAM_NAMES[number],
        "lower_trigram": lower,
        "upper_trigram": upper,
        "bits": list(bits),
    }


def derive(values: list[int]) -> dict[str, object]:
    """Derive the original and changed hexagrams from six line totals.

    Args:
        values: Six integers in ``{6, 7, 8, 9}``, ordered bottom-to-top.

    Raises:
        ValueError: If the count or any line value is invalid.
    """
    if len(values) != 6:
        raise ValueError("expected exactly six line values, ordered bottom-to-top")
    if any(type(value) is not int or value not in ORIGINAL_BIT for value in values):
        raise ValueError("each line value must be 6, 7, 8, or 9")

    original_bits = [ORIGINAL_BIT[value] for value in values]
    changed_bits = [CHANGED_BIT[value] for value in values]
    return {
        "values": list(values),
        "original": _identify(original_bits),
        "moving_lines": [index for index, value in enumerate(values, start=1) if value in (6, 9)],
        "changed": _identify(changed_bits),
    }
