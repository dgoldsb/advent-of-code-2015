"""Solve day 3."""
from aoc.helpers import time_it


def _do_instruction(c: str, current: tuple[int, int]) -> tuple[int, int]:
    match c:
        case "v":
            current = (current[0], current[1] - 1)
        case "^":
            current = (current[0], current[1] + 1)
        case "<":
            current = (current[0] - 1, current[1])
        case ">":
            current = (current[0] + 1, current[1])
    return current


@time_it
def part_a(input_: str):
    """How many houses receive at least one present?"""
    current = (0, 0)
    set_ = {current}
    for c in input_:
        current = _do_instruction(c, current)
        set_.add(current)
    return len(set_)


@time_it
def part_b(input_: str):
    """This year, how many houses receive at least one present?"""
    santa_current = (0, 0)
    santa = set()
    robot_santa_current = (0, 0)
    robot_santa = set()

    for i, c in enumerate(input_):
        robot = i % 2 == 1

        if robot:
            current = robot_santa_current
        else:
            current = santa_current

        current = _do_instruction(c, current)

        if robot:
            robot_santa_current = current
            robot_santa.add(robot_santa_current)
        else:
            santa_current = current
            santa.add(santa_current)

    return len(santa.union(robot_santa))
