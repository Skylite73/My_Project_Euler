# Project Euler 4

for i in range(1000000,0,-1):
    passes = True
    for j in range(len(str(i))):
        if str(i)[j] != str(i)[-(j+1)]:
            passes = False
    if passes:    
        for j in range(100,1000):
            if i % j == 0 and i/j < 1000:
                print(i,j,i/j)
