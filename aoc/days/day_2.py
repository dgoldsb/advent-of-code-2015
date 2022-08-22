"""Solve day 2."""
from aoc.helpers import ints, group, time_it


@time_it
def part_a(input_: str):
    """How many total square feet of wrapping paper should they order?"""
    total = 0
    for t in group(3, ints(input_)):
        sides = (
            t[0] * t[1],
            t[1] * t[2],
            t[0] * t[2],
        )
        total += 2 * sum(sides) + min(sides)
    return total


@time_it
def part_b(input_: str):
    """How many total feet of ribbon should they order?"""
    total = 0
    for t in group(3, ints(input_)):
        sides = (
            t[0] + t[1],
            t[1] + t[2],
            t[0] + t[2],
        )
        total += t[0] * t[1] * t[2] + 2 * min(sides)
    return total
