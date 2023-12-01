import pytest
from app.day01.parts import compute_part_1, compute_part_2

INPUT_TXT = """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            INPUT_TXT,
            142,
        )
    ],
)
def test_part_1(input_, expected):
    assert compute_part_1(input_) == expected


INPUT_TXT_2 = """\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            INPUT_TXT_2,
            281,
        )
    ],
)
def test_part_2(input_, expected):
    assert compute_part_2(input_) == expected
