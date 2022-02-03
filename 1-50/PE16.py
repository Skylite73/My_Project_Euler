# Project Euler <num>

import timeit
import math
from numba import njit

#@njit(fastmath=True)#, parallel=True)
def thing():
    print(sum([int(i) for i in str(2 ** 1000)]))
    

print("Time:", timeit.timeit("thing()", globals=globals(), number=1))
