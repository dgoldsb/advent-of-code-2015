"""Solve day 1."""
from aoc_py03 import count_char

from aoc.helpers import time_it


@time_it
def part_a(input_: str):
    """To what floor do the instructions take Santa?"""
    return count_char(input_, "(") - count_char(input_, ")")


@time_it
def part_b(input_: str):
    """What is the position of the character that causes Santa to first enter the basement?"""
    floor = 0
    for i, c in enumerate(input_):
        match c:
            case "(":
                floor += 1
            case ")":
                floor -= 1
            case _:
                raise RuntimeError()

        if floor == -1:
            return i + 1
