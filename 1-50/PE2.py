# Project Euler 2

num0 = 0
num1 = 1
total = 0

while num1 < 4000000:
    num0, num1 = num1, num1 + num0
    if num1 % 2 == 0:
        total += num1
print(total)
