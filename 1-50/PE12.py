# Project Euler 12

from timeit import timeit
from math import ceil
from numba import jit

@jit(nopython=True)#, parallel=True)
def thing():
    tri = [int(i*(i+1)/2) for i in range(1,100000)]
    for i in tri:
        lim = ceil((i+1)/2)
        #"""
        num = 1
        for j in range(1,lim):
            if i % j == 0:
                num += 1
        #"""
        #num = sum([1 if i % j == 0 else 0 for j in range(1,lim)]) + 1
        #num = sum(list(map(lambda j: 1 if i % j == 0 else 0, range(1,lim)))) + 1
        #print(i, num_factors, [i+1 for i, x in enumerate(factors) if x == 1])
        if num > 500:
            print("DONE:", i, num)
            break
print("time", timeit("thing()", globals=globals(), number=1))
