# Project Euler 17

import timeit
import math
from numba import njit


num_words1 = ['One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
num_words2 = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

#@njit(fastmath=True)#, parallel=True)
def thing():
    total = 0
    for i in range(1,1001):
        total += len(wordify(i))
        #print(i, len(wordify(i)), wordify(i))
    print(total)

def wordify(num):
    numstr = str(num)
    if len(numstr) == 1:
        return wordify1(num)
    elif len(numstr) == 2:
        return wordify2(num)
    elif len(numstr) == 3:
        return wordify3(num)
    elif len(numstr) == 4:
        return 'OneThousand'


def wordify1(num):
    return num_words1[int(str(num)[-1])-1]

def wordify2(num):
    dig = int(str(num)[-2:])
    if dig < 10:
        return wordify1(num)
    elif dig >= 10 and dig < 20:
        if dig == 10:
            return 'Ten'
        elif dig == 11:
            return 'Eleven'
        elif dig == 12:
            return 'Twelve'
        elif dig == 13:
            return 'Thirteen'
        elif dig == 15:
            return 'Fifteen'
        elif dig == 18:
            return 'Eighteen'
        else:
            return ''.join([wordify1(num),'teen'])
    else:
        if int(str(num)[-1]) == 0:
            return num_words2[int(str(num)[-2])-1]
        else:
            return ''.join([num_words2[int(str(num)[-2])-1], wordify1(num)])
        

def wordify3(num):
    numstr = str(num)
    if int(numstr[-2:]) == 0:
        return ''.join([wordify1(int(str(num)[0])),'Hundred'])
    return ''.join([wordify1(int(str(num)[0])),'HundredAnd',wordify2(num)])
    

print("Time:", timeit.timeit("thing()", globals=globals(), number=1))
