"""Project Euler <num>."""

try:
    """Works if ../Modules is in MYPYPATH or PYTHONPATH env vars"""
    from timer import timer
except ModuleNotFoundError:
    import os
    import sys
    script_path = os.path.realpath(os.path.dirname(__name__))
    os.chdir(script_path)
    sys.path.append("./Python-Debugging-Modules/")
    from timer import timer  # type: ignore
from debugger import debug, debug_table  # type: ignore
# from plotter import plotter  # type: ignore
# from numba import jit
# from math import pi, sin, cos
# import numpy as np


@timer
# @plotter(plot=True)
# @jit(nopython=True, fastmath=True, nogil=True)  # , parallel=True)
def main():
    """Run thing."""
    for i in range(10):
        var1 = i * 2
        var2 = i * 3
        debug(locals(), "[var1,var2]")
    print(debug_table())
    pass


if __name__ == '__main__':
    main()
