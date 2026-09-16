"""Cast three secure random coins for each of six lines exactly once."""

import json
import secrets
import sys


def cast_coins() -> dict[str, list[object]]:
    """Return 18 raw coins and their six bottom-to-top line totals.

    A random bit of 1 is heads (3); a random bit of 0 is tails (2).
    """
    coins = [3 if secrets.randbelow(2) == 1 else 2 for _ in range(18)]
    coin_groups = [coins[index:index + 3] for index in range(0, 18, 3)]
    return {
        "coins": coins,
        "coin_groups": coin_groups,
        "lines": [sum(group) for group in coin_groups],
    }


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    result = cast_coins()
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
