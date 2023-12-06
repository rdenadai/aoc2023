import sys
from math import prod

from app.support.utils import main, parse_module_to_day, timing


def parser_part_1(s: str) -> tuple[tuple[int, int], ...]:
    times, distances = s.splitlines()
    time = map(int, times.replace("Time:", "").split())
    distance = map(int, distances.replace("Distance:", "").split())
    return tuple(zip(time, distance))


@timing
def compute_part_1(s: str) -> int:
    races = parser_part_1(s)
    return prod(sum(1 for c in range(1, t) if ((t - c) * c) > d) for t, d in races)


def parser_part_2(s: str) -> tuple[int, int]:
    times, distances = s.splitlines()
    time = int("".join(times.replace("Time:", "").split()))
    distance = int("".join(distances.replace("Distance:", "").split()))
    return time, distance


@timing
def compute_part_2(s: str) -> int:
    t, d = parser_part_2(s)
    return sum(1 for c in range(1, t) if ((t - c) * c) > d)


if __name__ == "__main__":  # pragma: no cover
    module, day = parse_module_to_day(sys.modules[__name__].__package__)

    main(day, module, compute_part_1, compute_part_2)
