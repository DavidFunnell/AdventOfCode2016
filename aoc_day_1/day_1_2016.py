"""
This is day 1 of AOC 2016
"""

import typing
import pytest


def determine_direction(turn: str, current_direction: int) -> int:
    assert turn in ["R", "L"]
    if turn == "R":
        current_direction += 1
        return current_direction % 4
    else:
        current_direction -= 1
        return current_direction % 4


class Position:
    def __init__(self, x_position, y_position, current_direction):
        self.x_position = x_position
        self.y_position = y_position
        self.current_direction = current_direction


def move(pos: Position, input_direction: str, input_distance: int, attempt: bool, visited_positions):
    i = 0
    while i < input_distance:

        current_position = str(pos.x_position) + "," + str(pos.y_position)
        if attempt:
            if current_position in visited_positions:
                intersection_distance = abs(pos.x_position) + abs(pos.y_position)
                print("Answer to part 2: " + str(intersection_distance))
                attempt = False
            else:
                visited_positions[current_position] = 1

        # north
        if pos.current_direction == 0:
            if input_direction == "R":
                pos.x_position += 1
            else:
                pos.x_position -= 1
        # east
        elif pos.current_direction == 1:
            if input_direction == "R":
                pos.y_position -= 1
            else:
                pos.y_position += 1
        # south
        elif pos.current_direction == 2:
            if input_direction == "R":
                pos.x_position -= 1
            else:
                pos.x_position += 1
        # west
        elif pos.current_direction == 3:
            if input_direction == "R":
                pos.y_position += 1
            else:
                pos.y_position -= 1
        i += 1

    return pos, attempt, visited_positions


def final_location(pos: Position) -> int:
    result = abs(pos.x_position) + abs(pos.y_position)
    return result


def main():
    attempt = True
    data = open("day_1_data.txt", "r")
    movements = data.readlines()[0].split(", ")
    position = Position(0, 0, 0)
    visited_positions: typing.Dict[str, int] = {}

    for instruction in movements:
        direction = instruction[0]
        distance = int(instruction[1:])
        location, attempt, visited_positions = move(position, direction, distance, attempt, visited_positions)
        location.current_direction = determine_direction(direction, position.current_direction)

    final_distance = final_location(location)

    print("Answer to part 1: " + str(final_distance))


if __name__ == "__main__":
    main()
