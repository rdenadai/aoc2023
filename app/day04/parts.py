import sys
from functools import reduce
from itertools import chain
from typing import Generator

from app.support.utils import main, parse_module_to_day, timing

ParsedNumbers = tuple[Generator[int, None, None], Generator[int, None, None]]


def parse_numbers(numbers: str) -> ParsedNumbers:
    w_numbers, m_numbers = numbers.strip().split("|")
    return (int(n) for n in w_numbers.split()), (int(n) for n in m_numbers.split())


def parser(s: str) -> tuple[dict, dict]:
    lines = (s.strip() for s in s.splitlines())
    games: dict[int, ParsedNumbers] = {
        int(sline[0].replace("Card", "").strip()): parse_numbers(sline[1])
        for line in lines
        if (sline := line.split(":"))
    }
    matches = {(i + 1): len(set(card[1]).intersection(card[0])) for i, card in enumerate(games.values())}
    return games, matches


@timing
def compute_part_1(s: str) -> int:
    games, matches = parser(s)
    return sum(
        reduce(lambda x, _: x * 2, range(numbers), 1)
        for i, _ in enumerate(games.keys())
        if (numbers := matches.get(i + 1, 0) - 1) >= 0
    )


@timing
def compute_part_2(s: str) -> int:
    games, matches = parser(s)
    keys = games.keys()
    lgames = dict(zip(keys, [[1] for _ in range(len(games))]))
    for i in range(1, len(keys) + 1):
        for _ in lgames.get(i, None):
            for k in range(1, matches.get(i, 0) + 1):
                lgames[i + k].append(1)
    return sum(chain.from_iterable(lgames.values()))


if __name__ == "__main__":  # pragma: no cover
    module, day = parse_module_to_day(sys.modules[__name__].__package__)

    main(day, module, compute_part_1, compute_part_2)
