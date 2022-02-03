# Project Euler 9

import timeit

def thing():
    for i in range(1000):
        for j in range(1000):
            k = 1000 - i - j
            if i**2 + j**2 == k**2:
                print("ANSWER: ", i*j*k, i, j , k)
    
print("Time elapsed:", timeit.timeit("thing()", globals=globals(), number=1))

