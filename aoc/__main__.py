"""Runs and times all days."""
from aoc.days.day_1 import part_a, part_b
from aoc.helpers import get_input


def main():
    # TODO: Dynamic import of everything, try iterate over all days.
    print(part_a(get_input(2015, 1)))
    print(part_b(get_input(2015, 1)))


if __name__ == "__main__":
    main()
