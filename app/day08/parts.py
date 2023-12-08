import re
import sys
from itertools import cycle
from math import lcm
from typing import Callable

from app.support.utils import main, parse_module_to_day, timing


def parser(s: str) -> tuple[list, dict[str, list[str]]]:
    reg = re.compile(r"[\(\)]+")
    lines = s.splitlines()

    instructions = list(lines[0])

    partial_path = [
        {line[0]: re.sub(reg, "", line[1]).split(",")}
        for line in ["".join(line.split(" ")).split("=") for line in lines[1:] if line]
    ]
    path: dict[str, list[str]] = {}
    for p in partial_path:
        path |= p
    return instructions, path


def calculate_steps(initial_pos: str, stop_criteria: Callable, path: dict, instructions: list[str]) -> int:
    n_steps = 0
    pos = initial_pos
    for inst in cycle(instructions):
        n_steps += 1
        left, right = path.get(pos)
        if inst == "L":
            pos = left
        elif inst == "R":
            pos = right

        if stop_criteria(pos):
            break
    return n_steps


@timing
def compute_part_1(s: str) -> int:
    instructions, path = parser(s)

    def stop_criteria(pos: str) -> bool:
        return pos == "ZZZ"

    return calculate_steps("AAA", stop_criteria, path, instructions)


@timing
def compute_part_2(s: str) -> int:
    instructions, path = parser(s)

    def stop_criteria(pos: str) -> bool:
        return pos.endswith("Z")

    n_steps = [calculate_steps(p, stop_criteria, path, instructions) for p in path.keys() if p.endswith("A")]
    return lcm(*n_steps)

    # 12357789728873


if __name__ == "__main__":  # pragma: no cover
    module, day = parse_module_to_day(sys.modules[__name__].__package__)

    main(day, module, compute_part_1, compute_part_2)
