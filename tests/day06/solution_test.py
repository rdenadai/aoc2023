import pytest

from app.day06.parts import compute_part_1, compute_part_2

INPUT_TEXT = """\
Time:      7  15   30
Distance:  9  40  200"""


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            INPUT_TEXT,
            288,
        )
    ],
)
def test_part_1(input_, expected):
    assert compute_part_1(input_) == expected


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            INPUT_TEXT,
            71503,
        )
    ],
)
def test_part_2(input_, expected):
    assert compute_part_2(input_) == expected
