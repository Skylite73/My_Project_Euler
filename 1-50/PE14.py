# Project Euler 14

import timeit
import math
from numba import jit

@jit(nopython=True)#, parallel=True)
def thing():
    maxx = 0
    for i in range(1,1000001):
        n = i
        count = 1
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
            count += 1
        if count > maxx:
            ans, maxx = i, count
            #print(i, maxx)
    print(ans, maxx)
print("time", timeit.timeit("thing()", globals=globals(), number=1))
