"""
This is day 2 of AOC 2016
"""

import typing
import pytest


class Position:
    def __init__(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position


def code(pos: Position, instruction: str):
    if instruction == "U":
        if pos.y_position != 2:
            pos.y_position += 1
    if instruction == "R":
        if pos.x_position != 2:
            pos.x_position += 1
    if instruction == "D":
        if pos.y_position != 0:
            pos.y_position -= 1
    if instruction == "L":
        if pos.x_position != 0:
            pos.x_position -= 1
    return pos


def p2_code(pos: Position, instruction: str):
    if instruction == "U":
        if pos.x_position == 2:
            if pos.y_position != 4:
                pos.y_position += 1
        if pos.x_position == 1 or pos.x_position == 3:
            if pos.y_position != 3:
                pos.y_position += 1
    if instruction == "R":
        if pos.y_position == 2:
            if pos.x_position != 4:
                pos.x_position += 1
        if pos.y_position == 1 or pos.y_position == 3:
            if pos.x_position != 3:
                pos.x_position += 1
    if instruction == "D":
        if pos.x_position == 2:
            if pos.y_position != 0:
                pos.y_position -= 1
        if pos.x_position == 1 or pos.x_position == 3:
            if pos.y_position != 1:
                pos.y_position -= 1
    if instruction == "L":
        if pos.y_position == 2:
            if pos.x_position != 0:
                pos.x_position -= 1
        if pos.y_position == 1 or pos.y_position == 3:
            if pos.x_position != 1:
                pos.x_position -= 1
    return pos


def main():
    data = open("day_2_data.txt", "r")

    key_pad_locations: typing.Dict[str, str] = {
        "0,0": "7",
        "1,0": "8",
        "2,0": "9",
        "0,1": "4",
        "1,1": "5",
        "2,1": "6",
        "0,2": "1",
        "1,2": "2",
        "2,2": "3"
    }

    p2_key_pad_locations: typing.Dict[str, str] = {
        "0,2": "5",
        "1,1": "A",
        "1,2": "6",
        "1,3": "2",
        "2,0": "D",
        "2,1": "B",
        "2,2": "7",
        "2,3": "3",
        "2,4": "1",
        "3,1": "C",
        "3,2": "8",
        "3,3": "4",
        "4,2": "9"
    }

    starting_position = Position(1, 1)
    part_1_code = ""

    p2_starting_position = Position(0, 2)
    part_2_code = ""

    for data_lines in data:
        line = list(data_lines)
        for instruction in line:
            starting_position = code(starting_position, instruction)
            p2_starting_position = p2_code(p2_starting_position, instruction)

        coordinate = str(starting_position.x_position) + "," + str(starting_position.y_position)
        part_1_code += key_pad_locations[coordinate]

        p2_coordinate = str(p2_starting_position.x_position) + "," + str(p2_starting_position.y_position)
        part_2_code += p2_key_pad_locations[p2_coordinate]

    print("Answer to part 1: " + part_1_code)
    print("Answer to part 2: " + part_2_code)


if __name__ == "__main__":
    main()
