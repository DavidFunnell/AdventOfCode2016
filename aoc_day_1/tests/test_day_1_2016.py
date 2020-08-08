import pytest

from aoc_day_1.day_1_2016 import Position, determine_direction, location_history


def test_direction():
    assert determine_direction("R", 0) == 1

    with pytest.raises(AssertionError):
        determine_direction("l", 0)

    assert determine_direction("R", 3) == 0

    assert determine_direction("L", 0) == 3

    assert determine_direction("L", 2) == 1


def test_position():
    pos = Position(x_position=0, y_position=0, current_direction=0)
    print(pos.current_direction)
    pos.current_direction = 1
    print(pos.current_direction)
    assert False



def test_location_history():
    # pos = Position(x_position=0, y_position=0, current_direction=0)







