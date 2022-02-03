import timeit
from math import factorial
from numpy import arange
from numba import jit, njit

#@njit(fastmath=True)#, parallel=True)
def thing():
    a = factorial(100)
    total = sum([int(i) for i in str(a)])
    print(total)
print("Time:", timeit.timeit("thing()", globals=globals(), number=1))
