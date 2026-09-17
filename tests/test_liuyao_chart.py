import importlib.util
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_DIR = REPO_ROOT / "skills" / "traditional-divination-skill" / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from derive_liuyao_chart import build_chart, localize_cast_time, values_to_engine
from hexagrams import HEXAGRAM_NAMES, derive


class LineEncodingTests(unittest.TestCase):
    def test_values_convert_to_engine_contract(self):
        bits, moving = values_to_engine([8, 8, 9, 8, 8, 8])
        self.assertEqual(bits, "001000")
        self.assertEqual(moving, {3: "老阳"})

    def test_invalid_value_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "6, 7, 8, or 9"):
            values_to_engine([7, 7, 7, 7, 7, 5])


class TimezoneTests(unittest.TestCase):
    def test_sydney_standard_time_offset(self):
        cast_time = localize_cast_time("2026-09-17T15:42:00", "Australia/Sydney")
        self.assertEqual(int(cast_time.utcoffset().total_seconds() // 60), 600)

    def test_sydney_daylight_time_offset(self):
        cast_time = localize_cast_time("2026-10-17T15:42:00", "Australia/Sydney")
        self.assertEqual(int(cast_time.utcoffset().total_seconds() // 60), 660)


@unittest.skipUnless(importlib.util.find_spec("liuyao"), "liuyao-engine not installed")
class IntegratedChartTests(unittest.TestCase):
    def test_all_64_hexagram_names_agree_with_existing_engine(self):
        from liuyao.hexagram import cast_chart
        for integer in range(64):
            bits = f"{integer:06b}"
            values = [7 if bit == "1" else 8 for bit in bits]
            derived = derive(values)
            chart = cast_chart(bits, day_gan=0)
            with self.subTest(bits=bits):
                self.assertIn(HEXAGRAM_NAMES[derived["original"]["number"]], chart.name)

    def test_recorded_exam_cast_builds_reproducible_najia_chart(self):
        chart = build_chart(
            [8, 8, 9, 8, 8, 8],
            cast_time="2026-09-17T15:42:00",
            timezone_name="Australia/Sydney",
            category="考试",
            question="本次国考录用结束前的报考方向",
        )
        self.assertEqual(chart["hexagram"]["original"]["number"], 15)
        self.assertEqual(chart["hexagram"]["changed"]["number"], 2)
        self.assertEqual(chart["najia"]["primary"]["name"], "地山谦")
        self.assertEqual(chart["najia"]["changed"]["name"], "坤为地")
        self.assertEqual(chart["najia"]["yongShen"]["liuQin"], "官鬼")
        self.assertEqual(chart["najia"]["castTime"]["timezone"], "Australia/Sydney")
        self.assertEqual(chart["najia"]["castTime"]["utcOffsetMinutes"], 600)


if __name__ == "__main__":
    unittest.main()
