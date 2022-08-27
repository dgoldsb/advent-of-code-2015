"""Solve day 6."""
from aoc_py03 import count_on_lights, count_total_brightness

from aoc.helpers import ints, time_it


def parse_inputs(input_):
    rust_inputs = []
    for line in input_.split("\n"):
        edges = tuple(ints(line))
        match line:
            case str() as string if "toggle" in string:
                rust_inputs.append((edges, "t"))
            case str() as string if "turn on" in string:
                rust_inputs.append((edges, "n"))
            case str() as string if "turn off" in string:
                rust_inputs.append((edges, "f"))
            case _:
                pass
    return rust_inputs


@time_it
def part_a(input_: str):
    """After following the instructions, how many lights are lit?"""
    return count_on_lights(parse_inputs(input_))


@time_it
def part_b(input_: str):
    """What is the total brightness?"""
    return count_total_brightness(parse_inputs(input_))
