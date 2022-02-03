# Project Euler 10

import timeit
import math
from numba import jit

@jit(nopython=True, parallel=True)
def thing():
    primes = [2, 3, 5, 7]
    total = 2+3+5+7
    yucky = ["0","2","4","5","6","8"]
    for i in range(9,2000000,2):
        if str(i)[-1] not in yucky:
            passes = True
            for j in primes:
                if i % j == 0:
                    passes = False
                if j > math.sqrt(i):
                    break
            if passes:
                primes.append(i)
    print(sum(primes))

        
print("time", timeit.timeit("thing()", globals=globals(), number=1))
