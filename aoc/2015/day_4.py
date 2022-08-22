"""Solve day 4."""
from aoc_py03 import mine_advent_coin

from aoc.helpers import time_it


@time_it
def part_a(input_: str):
    """Santa needs help mining some AdventCoins."""
    return mine_advent_coin(input_, "0" * 5)


@time_it
def part_b(input_: str):
    """Now find one that starts with six zeroes."""
    return mine_advent_coin(input_, "0" * 6)
