# Project Euler 7

import timeit

def thing():
    primes = [2, 3, 5]
    yucky = ["0","2","4","5","6","8"]
    for i in range(2,2000000):
        if str(i)[-1] not in yucky:
            passes = True
            for j in primes:
                if i % j == 0:
                    passes = False
            if passes:
                primes.append(i)
                if len(primes) >= 9999 and len(primes) <= 10005:
                    print(len(primes),i)
            if len(primes) >= 10010:
                print("DONE")
                print(primes[0:10], primes[10000])
                return primes
        
print("time", timeit.timeit("thing()", globals=globals(), number=1))
