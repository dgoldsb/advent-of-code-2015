"""Solve day 7."""
from aoc.helpers import time_it


def parse_inputs(input_):
    for line in input_.split("\n"):
        yield line


def encoded_length(string: str) -> int:
    return len(string) + string.count("\\") + string.count("\"") + 2


@time_it
def part_a(input_: str):
    """What is the ... literals minus the ... memory for the values of the strings?"""
    total = 0
    for string in parse_inputs(input_):
        total += len(string) - len(eval(string))
    return total


@time_it
def part_b(input_: str):
    """Encode each code representation as a new string!"""
    total = 0
    for string in parse_inputs(input_):
        total += encoded_length(string) - len(string)
    return total
