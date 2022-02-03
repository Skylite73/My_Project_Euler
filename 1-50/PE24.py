"""Project Euler 24."""

try:
    """Works if ../Modules is in MYPYPATH or PYTHONPATH env vars"""
    from timer import timer
except ModuleNotFoundError:
    import os
    import sys
    script_path = os.path.realpath(os.path.dirname(__name__))
    os.chdir(script_path)
    sys.path.append("./Modules/")
    from timer import timer  # type: ignore
from debugger import debug, debug_table  # type: ignore
# from plotter import plotter  # type: ignore
# from numba import jit
import math
# import numpy as np


@timer
# @plotter(plot=True)
# @jit(nopython=True, fastmath=True, nogil=True)  # , parallel=True)
def main():
    """Run thing."""
    perms_left = math.factorial(10)
    numbers = [i for i in range(10)]
    part_of_mil = 1000000
    for i in range(9, 0, -1):
        perms_left = perms_left // i
        part_of_mil = part_of_mil // i
        portion = part_of_mil / perms_left
        index = portion * len(numbers) % 1
        try:
            digit = numbers[index]
            numbers.pop(index)
        except Exception:
            digit = "Failed"

        debug(
            locals(), "[i, perms_left, part_of_mil, portion, index, digit, numbers]")
    debug_table()
    pass


if __name__ == '__main__':
    main()
