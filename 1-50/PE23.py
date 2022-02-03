# Project Euler <num>
# Find the sum of all the numbers which can not be written as the sum of two abundant numbers
# Where an abundant number is a number such that the sum of its factors is greater than the number


from timeit import timeit
from math import sqrt, ceil
from numba import jit, prange
#import numpy as np


@jit(nopython=True, fastmath=True, nogil=True)  # , parallel=True)
def factorise(num: int) -> int:
    factors = []
    if sqrt(num) % 1 == 0:
        factors.append(int(sqrt(num)))
    for j in prange(1, ceil(sqrt(num))):
        if num % j == 0:
            factors.append(j)
    factors_new = []
    for j in factors:
        if j != 1:
            factors_new.append(num // j)
    joined = factors
    joined += [i for i in (factors_new) if i not in joined]
    #print(joined, factors, factors_new)
    #print(sum(joined), sum(factors), sum(factors_new))
    return sum(joined)


@jit(fastmath=True, nopython=True, nogil=True)  # , parallel=True)
def thing():
    abundants = []
    for i in range(1, 30000):
        factor_sum = factorise(i)
        if factor_sum > i:
            abundants.append(i)
    print(abundants)
    lst = []
    # The first way i tried (which i usually go for). It it brute force on all numbers
    """
    for i in range(30000):
        for j in abundants:
            if (i - j) in abundants:
                break
            if j > i:
                lst.append(i)
                break
    print(lst)
    print(sum(lst))
    """
    # The better way to do it. You find the negative by iterating all the things you know. Much better
    mask = []
    for i in range(len(abundants)):
        for j in range(i, len(abundants)):
            mask.append(abundants[i]+abundants[j])
    print(sum([i for i in range(30000) if i not in mask]))


def test():

    x = input("Num: ")
    while x:
        print(factorise(int(x)))
        """
        i = int(x)
        for j in abundants:
            if j > i:
                print("Not a sum. This should only come up once")
                break
            #print(i, j, i-j, (i - j) in abundants)
            print(i, j, i-j, (i-j) in abundants)
            if (i - j) in abundants:
                print("A sum. This should only come up once")
                break
        abundants = []
        for i in range(29000):
            factor_sum = factorise(i)
            if factor_sum > i:
                abundants.append(i)
        print(abundants)
        """
        x = input("Num: ")


#print("jshdkf", pt())
print("Time:", timeit("thing()", globals=globals(), number=1))

#print(factorise(196))
