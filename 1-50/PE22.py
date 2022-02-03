# Project Euler <num>

import timeit
#from math import sqrt
#from numba import jit

alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def alph_num(word):
    num = 0
    for i in word:
        num += alph.index(i)+1
    return num

#@njit  # (fastmath=True, parallel=True)


def thing():
    with open("resources/PE22.txt", "r") as f:
        text = f.read().replace('"', '').split(',')
        text.sort()
    total = 0
    for i, word in enumerate(text):
        num = alph_num(word.lower()) * (i+1)
        total += num
        #print(i+1, word, alph_num(word.lower()), num)
    print(total)


print("Time:", timeit.timeit("thing()", globals=globals(), number=1))
