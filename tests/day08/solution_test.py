import pytest

from app.day08.parts import compute_part_1, compute_part_2

INPUT_TEXT = """\
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""


INPUT_TEXT_2 = """\
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            INPUT_TEXT,
            2,
        ),
        (
            INPUT_TEXT_2,
            6,
        ),
    ],
)
def test_part_1(input_, expected):
    assert compute_part_1(input_) == expected


INPUT_TEXT_PART_2 = """\
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            INPUT_TEXT_PART_2,
            6,
        ),
    ],
)
def test_part_2(input_, expected):
    assert compute_part_2(input_) == expected
