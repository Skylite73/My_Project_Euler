import timeit
from math import floor, sqrt
#from numpy import arange
#from numba import jit


def factorise(num):
    factors = set()
    for j in range(1, floor(sqrt(num))):
        if num % j == 0:
            factors.add(j)
    factors_new = set()
    for j in factors:
        if j != 1:
            factors_new.add(num / j)
    factors = factors | factors_new
    return factors

#@njit(fastmath=True)#, parallel=True)


def thing():
    amicables = set()
    for i in range(10000):
        factors_num = factorise(i)
        pair = sum(factors_num)
        factors_pair = factorise(pair)
        if sum(factors_pair) == i and i != pair:
            amicables.add(frozenset([i, pair]))
    print(amicables)
    total = sum([sum(i) for i in amicables])
    print(total)


print("Time:", timeit.timeit("thing()", globals=globals(), number=1))
