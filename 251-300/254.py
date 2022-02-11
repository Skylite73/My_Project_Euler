"""Project Euler 254."""

try:
    """Works if Python-Debugging-Modules/ is in MYPYPATH or PYTHONPATH"""
    from Modules.timer import timer
    from Modules.debugger import Debugger
    # from Modules.plotter import plotter
except ModuleNotFoundError:
    """Temporarily adds modules to Python PATH"""
    import os
    import sys
    script_path = os.path.abspath(os.path.dirname(__file__))
    module_path = os.path.join(script_path, "Modules")  # Change to module path
    sys.path.append(module_path)
    from timer import timer
    from debugger import Debugger
    # from plotter import plotter
# from numba import jit
# from math import pi, sin, cos
# import numpy as np
import multiprocessing as mp
import timeit
import math
import itertools
from itertools import combinations_with_replacement as comb
from functools import reduce, cache, lru_cache
import cProfile


def main():
    """Run thing."""
    dict = sf_list(max_num=25, digits=8)
    print("Dict done!")
    ans = sum([digit_sum(dict[i]) for i in dict])
    print(ans, dict)
    # print(timeit.repeat("run_async(f)",
    #                    number=15, repeat=1, globals=globals()))


def sf_list(max_num, digits):
    num_left = list(range(1, max_num+1))
    num_dict = {}
    print("Starting...")
    for i in get_item_gen(digits):
        num = sf(i)
        if num in num_left:
            num_dict[num] = i
            num_left.remove(num)
            print(f"Got {num} ({i})")
            if len(num_left) == 0:
                break
    if len(num_left):
        print("NOT ENOUGH DIGITS!")
        raise Exception
    return num_dict


def get_item_gen(digits):
    print("Making list")
    with mp.Pool() as pool:
        item_gen = pool.imap(mapper, comb(range(10), digits), 10)
    print("Trying to print")
    [print(i) for i in item_gen]
    print("List done.")

    return item_gen


def mapper(a):
    print("trying to map " + a)
    b = reduce(reducer, (i for i in a))
    print(f"Mapping {a} to {b}")
    return b


@lru_cache
def reducer(x, y):
    try:
        return x * 10 ** (1 + math.floor(math.log10(y))) + y
    except ValueError:
        return x


def sf(num):
    return digit_sum(f(num))


@lru_cache
def digit_sum(num):
    return sum(map(int, str(num)))


def f(num):
    """."""
    return sum(map(math.factorial, map(int, str(num))))


if __name__ == '__main__':
    cProfile.run("main()")


############################ Rejection Corner #################################

def run_async(func):
    with mp.Pool() as pool:
        sum(pool.imap(func, range(10 ** 6), 10 ** 4))


def add_0(num):
    length: int = math.floor(math.log10(num))
    size = 10 ** length
    leading: int = num // size
    rest: int = num % size
    new: int = leading * size * 10 + rest
    print(num, new)
    return new


def zeroes(digits, inp_lst):
    """Turns out that you don't need to include this... :|."""
    print("Filtering.")
    zeroable = filter(lambda x: math.floor(math.log10(x))+1 < digits, inp_lst)
    print("Adding zeroes.")
    with mp.Pool() as pool:
        new_nums = pool.imap(add_0, zeroable, len(list(zeroable))//11+1)
    print("Adding on.")
    inp_list = itertools.chain(inp_lst, new_nums)
    print("Sorting.")
    inp_list = sorted(inp_lst)
    print(inp_list)
