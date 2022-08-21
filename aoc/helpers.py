"""Helpers in the project."""
import time
from functools import lru_cache
from pathlib import Path

INPUTS = Path(__file__).parents[1] / "inputs"


@lru_cache
def get_input(year: int, day: int) -> str:
    """Get input, first try AoC token, then input file."""
    # TODO: AoC token first.
    return (INPUTS / str(year) / f"{day}.txt").read_text()


def time_it(func):
    def wrapped(*args, **kwargs):
        begin = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        # TODO: Track total and breakdown, print function.
        print(f"Total time taken in {func.__name__}: {end - begin}")
        return result

    return wrapped
