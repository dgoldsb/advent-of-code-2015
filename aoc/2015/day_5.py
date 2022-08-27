"""Solve day 5."""
import re

from aoc.helpers import time_it

DUPLICATE = re.compile(r"(.)\1")
AEIOU = re.compile(r"[aieou].*[aieou].*[aieou]")
AB_CD_PQ_XY = re.compile(r"ab|cd|pq|xy")


def _is_nice(string) -> bool:
    return (
        re.search(DUPLICATE, string) is not None
        and re.search(AEIOU, string) is not None
        and re.search(AB_CD_PQ_XY, string) is None
    )


XY_XY = re.compile(r"([a-z][a-z]).*\1")
EFE = re.compile(r"([a-z]).\1")


def _is_new_nice(string) -> bool:
    return re.search(XY_XY, string) is not None and re.search(EFE, string) is not None


@time_it
def part_a(input_: str):
    """How many strings are nice?"""
    return len(list(filter(lambda s: _is_nice(s), iter(input_.split("\n")))))


@time_it
def part_b(input_: str):
    """How many strings are nice under these new rules?"""
    return len(list(filter(lambda s: _is_new_nice(s), iter(input_.split("\n")))))
