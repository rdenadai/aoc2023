import sys
from math import sqrt

from app.support.utils import main, parse_module_to_day, timing


def to_matrix(s):
    return [list(line) for line in s.splitlines()]


def check_if_symbol(el):
    return True if el != "." and not el.isdigit() else False


def check_if_number(el):
    return True if el.isdigit() else False


POSITION_PAIRS = (
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),
    (-1, 0),
    (0, -1),
    (0, 1),
    (1, 0),
)


def has_symbol_on_surrounders(i, k, w, h, matrix):
    positions = []
    if i > 0 or k > 0:
        for x, y in POSITION_PAIRS:
            if i + x < w and k + y < h and check_if_symbol(matrix[i + x][k + y]):
                positions.append(True)
    return any(positions)


@timing
def compute_part_1(s: str) -> int:
    nums = []
    matrix = to_matrix(s)
    w, h = len(matrix[0]), len(matrix)
    for i, line in enumerate(matrix):
        hold_num = []
        found_symbol = False
        for k, char in enumerate(line):
            is_number = check_if_number(char)
            if is_number:
                hold_num.append(char)
                if has_symbol_on_surrounders(i, k, w, h, matrix):
                    found_symbol = True
            if found_symbol and not is_number or found_symbol and k == w - 1:
                nums.append(int("".join(hold_num)))
                found_symbol = False
            if not is_number:
                hold_num = []
    return sum(nums)


def are_adjacent(x1, y1, x2, y2):
    manhattan_distance = abs(x2 - x1) + abs(y2 - y1)
    euclidean_distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return manhattan_distance == 1 or euclidean_distance == sqrt(2)


@timing
def compute_part_2(s: str) -> int:
    # print("------------------------")
    # import re

    # num_coords = []
    # symbol_coords = []
    # for x, line in enumerate(s.split("\n")):
    #     nums = re.finditer(r"\d+", line)
    #     for n in nums:
    #         coords = []
    #         for i in range(len(n.group())):
    #             coords.append((x, n.start() + i))
    #         num_coords.append([int(n.group()), coords])
    #     symbols = re.finditer(r"[*]", line)
    #     for s in symbols:
    #         symbol_coords.append([s.group(), (x, s.start()), []])
    # for n in num_coords:
    #     for c in n[1]:
    #         for s in symbol_coords:
    #             if abs(c[0] - s[1][0]) <= 1 and abs(c[1] - s[1][1]) <= 1:
    #                 s[2].append(n) if n not in s[2] else 0
    #                 break

    # print([[s[2][0][0], s[2][1][0]] for s in symbol_coords if len(s[2]) == 2])
    # print("Day 03 Part 2:", sum([s[2][0][0] * s[2][1][0] for s in symbol_coords if len(s[2]) == 2]))

    matrix = to_matrix(s)
    w, h = len(matrix[0]), len(matrix)

    symbols, nums = [], []
    for i, line in enumerate(matrix):
        positions, hold_num, found_symbol = [], [], False
        for k, char in enumerate(line):
            if char == "*":
                symbols.append((i, k))
                if hold_num: # Flush the number, if its not empty
                    nums.append([int("".join(hold_num)), positions])
                hold_num, positions = [], []
            else:
                is_number = check_if_number(char)
                if is_number: # if its a number lets keep it in memory
                    hold_num.append(char)
                    positions.append([i, k])
                    if has_symbol_on_surrounders(i, k, w, h, matrix):
                        found_symbol = True
                if (found_symbol and not is_number) or (found_symbol and k == w - 1):
                    if hold_num: # Flush the number, if its not empty
                        nums.append([int("".join(hold_num)), positions])
                    found_symbol = False
                if not is_number: # If its a dot (.) or other char
                    hold_num, positions = [], []

    gears_ratios = []
    for i, symbol in enumerate(symbols):
        gear: list[int] = []
        for num, positions in nums:
            for pos in positions:
                if are_adjacent(*[*pos, *symbol]):
                    gear.append(num)
                    break
        if len(gear) == 2:
            gears_ratios.append(gear)
    return sum((gear[0] * gear[1] for gear in gears_ratios))


if __name__ == "__main__":  # pragma: no cover
    module, day = parse_module_to_day(sys.modules[__name__].__package__)

    main(day, module, compute_part_1, compute_part_2)
