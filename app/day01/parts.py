import sys

from app.support.utils import main, parse_module_to_day, timing

WORDS_TO_NUMBERS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def _compute(input_: str) -> list[list[str]]:
    numbers = []
    for line in input_.splitlines():
        part = [char for char in line if char.isdigit()]
        numbers.append(part or ["0"])
    return numbers


def _compute_2(input_: str) -> list[list[str]]:
    numbers = []
    for line in input_.splitlines():
        # I don't like this solution ... but it was the fastest I could come up with
        for k, v in WORDS_TO_NUMBERS.items():
            line = line.replace(k, f"{k}{v}{k}")
        part = [char for char in line if char.isdigit()]
        numbers.append(part or ["0"])
    return numbers


@timing
def compute_part_1(input_: str) -> int:
    numbers: list[list[str]] = _compute(input_)
    return sum(int(f"{n[0]}{n[-1]}") for n in numbers)


@timing
def compute_part_2(input_: str) -> int:
    numbers: list[list[str]] = _compute_2(input_)
    return sum(int(f"{n[0]}{n[-1]}") for n in numbers)


if __name__ == "__main__":  # pragma: no cover
    module, day = parse_module_to_day(sys.modules[__name__].__package__)

    main(day, module, compute_part_1, compute_part_2)
