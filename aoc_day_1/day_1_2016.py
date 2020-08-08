"""
This is day 1 of AOC 2016
"""

import math
import typing
import pytest

open("day_1_part_2_data.txt", "w").close()



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


def move(pos: Position, input_direction: str, input_distance: int) -> Position:
    i = 0
    while i < input_distance:
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
        #adding each position to a txt file as I go through each step
        coordinates = open("day_1_part_2_data.txt", "a")
        coordinates.write(str(pos.x_position) + "," + str(pos.y_position) + "\n")
        coordinates.close()
        #setting the current location as a string for comparison
        current_spot = str(pos.x_position) + "," + str(pos.y_position)
        first_intersection(current_spot)


        # coordinates = open("day_1_part_2_data.txt", "r")
        # print(coordinates.readlines())
        # for steps in coordinates.readlines():
        #     if steps == "1,-1":
        #         print("Yep!!!")
            # if steps == current_spot:
            #     interception_distance = abs(pos.x_position) + abs(pos.y_position)
            #     print("interception distance: " + interception_distance)
    return pos


def final_location(pos: Position) -> int:
    result = abs(pos.x_position) + abs(pos.y_position)
    return result


def first_intersection(current_spot):
    coordinates = open("day_1_part_2_data.txt", "r")
    stops = coordinates.readlines()
    incomplete = True

    if incomplete:
        for steps in stops:
            if "1,-1" in steps:
                print((steps[0]))


def main():
    data = open("day_1_data.txt", "r")
    movements = data.readlines()[0].split(", ")
    position = Position(0, 0, 0)

    for instruction in movements:
        direction = instruction[0]
        distance = int(instruction[1:])
        location = move(position, direction, distance)
        location.current_direction = determine_direction(direction, position.current_direction)

    final_distance = final_location(location)

    # first_intersection()

    print(final_distance)


if __name__ == "__main__":
    main()
