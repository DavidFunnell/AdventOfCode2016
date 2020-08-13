"""
This is day 3 of AOC 2016
"""

import typing
import pytest


def triangle(lines: str, num_of_triangles):
    triangle_sides = lines.split()
    triangle_sides.sort()
    if int(triangle_sides[0]) + int(triangle_sides[1]) > int(triangle_sides[2]):
        if int(triangle_sides[1]) + int(triangle_sides[2]) > int(triangle_sides[0]):
            if int(triangle_sides[2]) + int(triangle_sides[0]) > int(triangle_sides[1]):
                num_of_triangles += 1
    return num_of_triangles


def main():
    data = open("day_3_data.txt", "r")
    num_of_triangles = 0
    i = 0

    for lines in data:
        i += 1
        num_of_triangles = triangle(lines, num_of_triangles)

    print(num_of_triangles)


if __name__ == "__main__":
    main()
