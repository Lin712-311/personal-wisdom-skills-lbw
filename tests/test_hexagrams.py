import json
import subprocess
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_DIR = REPO_ROOT / "skills" / "traditional-divination-skill" / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from cast_coins import cast_coins
from hexagrams import HEXAGRAM_NAMES, KING_WEN, TRIGRAMS, derive


class HexagramTests(unittest.TestCase):
    def test_all_young_yang_is_qian_without_change(self):
        result = derive([7, 7, 7, 7, 7, 7])
        self.assertEqual(result["original"]["number"], 1)
        self.assertEqual(result["original"]["name"], "乾")
        self.assertEqual(result["changed"]["number"], 1)
        self.assertEqual(result["moving_lines"], [])

    def test_all_old_yin_changes_kun_to_qian(self):
        result = derive([6, 6, 6, 6, 6, 6])
        self.assertEqual(result["original"]["number"], 2)
        self.assertEqual(result["changed"]["number"], 1)
        self.assertEqual(result["moving_lines"], [1, 2, 3, 4, 5, 6])

    def test_bottom_yang_rest_yin_is_returning(self):
        result = derive([7, 8, 8, 8, 8, 8])
        self.assertEqual(result["original"]["number"], 24)
        self.assertEqual(result["original"]["lower_trigram"], "震")
        self.assertEqual(result["original"]["upper_trigram"], "坤")

    def test_old_yang_changes_to_yin(self):
        result = derive([9, 7, 7, 7, 7, 7])
        self.assertEqual(result["original"]["number"], 1)
        self.assertEqual(result["changed"]["number"], 44)
        self.assertEqual(result["moving_lines"], [1])

    def test_king_wen_table_covers_every_hexagram_once(self):
        numbers = [
            number
            for lower_lookup in KING_WEN.values()
            for number in lower_lookup.values()
        ]
        self.assertEqual(len(TRIGRAMS), 8)
        self.assertEqual(set(TRIGRAMS.values()), set(KING_WEN))
        self.assertTrue(all(set(row) == set(TRIGRAMS.values()) for row in KING_WEN.values()))
        self.assertEqual(sorted(numbers), list(range(1, 65)))
        self.assertEqual(sorted(HEXAGRAM_NAMES), list(range(1, 65)))

    def test_all_64_static_bit_patterns_match_lookup_table(self):
        trigram_bits = {name: bits for bits, name in TRIGRAMS.items()}
        for upper, lower_lookup in KING_WEN.items():
            for lower, expected_number in lower_lookup.items():
                bits = trigram_bits[lower] + trigram_bits[upper]
                values = [7 if bit == "1" else 8 for bit in bits]
                with self.subTest(upper=upper, lower=lower):
                    result = derive(values)
                    self.assertEqual(result["original"]["number"], expected_number)
                    self.assertEqual(result["original"]["name"], HEXAGRAM_NAMES[expected_number])
                    self.assertEqual(result["changed"], result["original"])
                    self.assertEqual(result["moving_lines"], [])

    def test_rejects_wrong_length(self):
        with self.assertRaisesRegex(ValueError, "exactly six"):
            derive([7, 8])

    def test_rejects_invalid_value(self):
        with self.assertRaisesRegex(ValueError, "6, 7, 8, or 9"):
            derive([7, 7, 7, 7, 7, 5])

    def test_rejects_boolean_even_though_bool_is_an_int_subclass(self):
        with self.assertRaisesRegex(ValueError, "6, 7, 8, or 9"):
            derive([7, 7, 7, 7, 7, True])


class CoinCastingTests(unittest.TestCase):
    @patch("cast_coins.secrets.randbelow", side_effect=[0, 1] * 9)
    def test_cast_records_exactly_18_secure_coin_results(self, randbelow):
        result = cast_coins()

        self.assertEqual(randbelow.call_count, 18)
        randbelow.assert_called_with(2)
        self.assertEqual(len(result["coins"]), 18)
        self.assertEqual(result["coins"], [2, 3] * 9)
        self.assertEqual(result["lines"], [7, 8, 7, 8, 7, 8])
        self.assertEqual(result["coin_groups"], [[2, 3, 2], [3, 2, 3]] * 3)
        self.assertRegex(result["generated_at"], r"^\d{4}-\d{2}-\d{2}T.*\+00:00$")


class CliTests(unittest.TestCase):
    def test_derive_cli_emits_utf8_json(self):
        completed = subprocess.run(
            [sys.executable, str(SCRIPT_DIR / "derive_hexagram.py"), *(["7"] * 6)],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        result = json.loads(completed.stdout)
        self.assertEqual(result["original"]["name"], "乾")
        self.assertEqual(result["moving_lines"], [])


if __name__ == "__main__":
    unittest.main()
