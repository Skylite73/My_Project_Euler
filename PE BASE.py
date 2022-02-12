"""Project Euler <num>."""

try:
    """Works if Python-Debugging-Modules/ is in MYPYPATH or PYTHONPATH"""
    from Modules.debugger import Debugger
    # from Modules.plotter import plotter
except ModuleNotFoundError:
    """Temporarily adds modules to Python PATH"""
    import os
    import sys
    script_path = os.path.abspath(os.path.dirname(__file__))
    module_path = os.path.join(script_path, "Modules")  # Change to module path
    sys.path.append(module_path)
    from debugger import Debugger
    # from plotter import plotter
# from modules.debugger import Debugger
import cProfile
import timeit
# from numba import jit
# from math import pi, sin, cos
# import numpy as np

# @jit(nopython=True, fastmath=True, nogil=True)  # , parallel=True)


def main():
    """Run thing."""
    d = Debugger()
    for i in range(10):
        var1 = i * 2
        var2 = i * 3
        d.debug(locals(), "[var1,var2]")
    d.table()
    pass


if __name__ == '__main__':
    if __name__ == '__main__':
        pr = cProfile.run("""print(min(timeit.repeat("main()",
                                number=1, repeat=1,
                                 globals=globals())))""", sort='tottime')
