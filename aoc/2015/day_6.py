"""Solve day 6."""
from aoc.helpers import ints, time_it


@time_it
def part_a(input_: str):
    """After following the instructions, how many lights are lit?"""
    # TODO: To Rust, was 3-4 seconds.
    on_lights = set()
    for line in input_.split("\n"):
        edges = tuple(ints(line))
        match line:
            case str() as string if "toggle" in string:
                for i in range(edges[0], edges[2] + 1):
                    for j in range(edges[1], edges[3] + 1):
                        tuple_ = (i, j)
                        if tuple_ in on_lights:
                            on_lights.remove(tuple_)
                        else:
                            on_lights.add(tuple_)
            case str() as string if "turn on" in string:
                for i in range(edges[0], edges[2] + 1):
                    for j in range(edges[1], edges[3] + 1):
                        on_lights.add((i, j))
            case str() as string if "turn off" in string:
                for i in range(edges[0], edges[2] + 1):
                    for j in range(edges[1], edges[3] + 1):
                        try:
                            on_lights.remove((i, j))
                        except KeyError:
                            pass
            case _:
                pass
    return len(on_lights)
