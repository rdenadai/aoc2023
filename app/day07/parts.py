import sys
from typing import Any
from collections import Counter

from app.support.utils import main, parse_module_to_day, timing

CARDS_PART_1 = dict(
    zip(
        (
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "T",
            "J",
            "Q",
            "K",
            "A",
        ),
        range(1, 14),
    )
)

CARDS_PART_2 = dict(
    zip(
        (
            "J",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "T",
            "Q",
            "K",
            "A",
        ),
        range(1, 14),
    )
)


def parser(s: str) -> dict[str, int]:
    return {n[0]: int(n[1]) for line in s.splitlines() if len(n := line.split()) > 0}


def sort_by_type(lst: list) -> None:
    n = len(lst) - 1
    i, is_sorted = 0, True
    while True:
        if i >= n:
            if is_sorted:
                break
            i, is_sorted = 0, True

        ac, nx = lst[i], lst[i + 1]
        if ac.get("sort") > nx.get("sort"):
            lst[i], lst[i + 1] = nx, ac
            is_sorted = False
        i += 1


def generate_ranks_part_1(hands: dict[str, int]) -> list[dict[str, Any]]:
    ranks = [
        {
            "card": card,
            "bid": bid,
            "sort": int(
                "".join(sorted([str(v) for k, v in Counter(card).items()], reverse=True)).ljust(5, "0")
                + "".join([str(CARDS_PART_1[s]).zfill(2) for s in card])
            ),
        }
        for card, bid in hands.items()
    ]
    sort_by_type(ranks)
    return ranks


def generate_ranks_part_2(hands: dict[str, int]) -> list[dict[str, Any]]:
    ranks = []
    for card, bid in hands.items():
        new_card = card  # Keep original card
        # Lets replace "J" with the most common card
        c = Counter(card)
        _ = c.pop("J") if "J" in c else None
        if len(mc := c.most_common(1)):
            new_card = card.replace("J", mc[0][0])
        ranks.append(
            {
                "card": card,
                "bid": bid,
                "sort": int(
                    (
                        f'{"".join(sorted([str(v) for _, v in Counter(new_card).items()], reverse=True)).ljust(5, "0")}'
                        f'{"".join([str(CARDS_PART_2[s]).zfill(2) for s in card])}'
                    )
                ),
            }
        )
    sort_by_type(ranks)
    return ranks


@timing
def compute_part_1(s: str) -> int:
    hands = parser(s)
    ranks = generate_ranks_part_1(hands)
    return sum((rank.get("bid", 1) * (i + 1)) for i, rank in enumerate(ranks))


@timing
def compute_part_2(s: str) -> int:
    hands = parser(s)
    ranks = generate_ranks_part_2(hands)
    return sum((rank.get("bid", 1) * (i + 1)) for i, rank in enumerate(ranks))


if __name__ == "__main__":  # pragma: no cover
    module, day = parse_module_to_day(sys.modules[__name__].__package__)

    main(day, module, compute_part_1, compute_part_2)
