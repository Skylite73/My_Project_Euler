import timeit
from math import sqrt
from numpy import arange
from numba import jit, njit

#@njit(fastmath=True)#, parallel=True)
def thing():
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    month_change = list(map(lambda x: x % 7, month_days))
    total = 0
    year = 1900
    day = 1
    while year < 2001:
        for i in range(12):
            if day == 0 and year > 1900:
                total += 1
            if i == 1 and year % 4 == 0:
                day += 1
            else:
                day += month_change[i]
            day %= 7
        year += 1
    print(total)
print("Time:", timeit.timeit("thing()", globals=globals(), number=1))
