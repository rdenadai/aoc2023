import pytest

from app.day03.parts import compute_part_1, compute_part_2

INPUT_TEXT = """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            INPUT_TEXT,
            4361,
        ),
    ],
)
def test_part_1(input_, expected):
    assert compute_part_1(input_) == expected


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            INPUT_TEXT,
            467835,
        ),
    ],
)
def test_part_2(input_, expected):
    assert compute_part_2(input_) == expected
