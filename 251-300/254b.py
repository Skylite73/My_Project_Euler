"""Project Euler 254."""

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
    #print({i: m.factorial(i) for i in range(10)})
    print(sg(50))
    #[print(ssg(i)) for i in range(15)]


@lru_cache(65536)
def digit_sum(num):
    return sum(map(int, str(num)))


def sf(n_gen, pool=None, chunk=None):
    """Take n_gen and return sf_n_gen.

    Fact for each digit
    Sum Facts
    DS sum
    """
    try:
        return pool.imap(mapper_sf_n, n_gen, chunk)
    except ValueError:
        print("EXCEPTION!")
    #return digit_sum(sum(map(m.factorial, map(int, str(n)))))


def mapper_sf_n(n):
    int_gen = map(int, str(n))
    return digit_sum(sum(map(m.factorial, int_gen)))


def sg(i, digits=1):
    chunk = m.comb(10+digits-1, digits)//100+1
    with mp.Pool() as pool:
        n_gen = pool.imap(mapper_n, combs(range(10), digits), chunk)
        # print(i, n_gen)
        for sf_n in sf(n_gen, pool, chunk):
            if sf_n == i:
                return sf_n
            #print(4)
    return sg(i, digits+1)


def mapper_n(gen):
    str_lst = map(str, gen)
    return int(''.join(str_lst))


def ssg(num):
    total = 0
    for i in range(1, 1+num):
        thing = sg(i)
        print(i, thing)
        total += thing
    return total


if __name__ == '__main__':
    cmd = """print("Time:",min(timeit.repeat("main()",
                        number=1, repeat=1, globals=globals())))"""
    if 1:
        pr = cProfile.run(cmd, sort='tottime')
    else:
        exec(cmd)
