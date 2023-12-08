import pytest

from app.day07.parts import compute_part_1, compute_part_2

INPUT_TEXT = """\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            INPUT_TEXT,
            6440,
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
            5905,
        ),
    ],
)
def test_part_2(input_, expected):
    assert compute_part_2(input_) == expected
