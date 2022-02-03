# Project Euler 3



def search(num, lst):
    if num in lst:
        return lst
    lst.append(num)
    for i in range(2,min(1000000,num)):
        if num % i == 0:
            print(num, i, num / i)
            search(int(num / i),lst)
            search(int(i), lst)
            break
    return lst
i = input("Input: ")
while input:
    print("lst",search(int(i), []))
    i = input("Input: ")
