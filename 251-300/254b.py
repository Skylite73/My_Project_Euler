"""Project Euler 254."""


from Modules.timer import timer
from Modules.debugger import Debugger
import multiprocessing as mp
import timeit
import math as m
import itertools as it
import operator as op
from itertools import combinations_with_replacement as combs
from functools import reduce, lru_cache
import cProfile


def main():
    """Run thing."""


if __name__ == '__main__':
    pr = cProfile.run("""print(min(timeit.repeat("main()",
                            number=1, repeat=1,
                             globals=globals())))""", sort='tottime')
