# Project Euler 15

import timeit
from math import comb
from numba import njit

@njit( #, parallel=true)
def thing():
    # n is number of total moves 
    # k is number of total moves to get there
    # p is probability of going right
    # Total for 40 moves
    n = 40
    k = 40
    p = 0.5
    total = binom(p,n,k)
    print(total)

@jit(nopython=True)
def binom(p,n,k):
    return comb(n,k) * (p ** n) * ((1-p) ** (n-k))
    
print("time", timeit.timeit("thing()", globals=globals(), number=1))
