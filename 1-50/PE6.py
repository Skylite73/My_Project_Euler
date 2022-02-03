# Project Euler 6

numbers = [i for i in range(1,101)]

SSQ = sum([i*i for i in numbers])
SQS = sum([i for i in numbers]) ** 2
diff = SQS - SSQ

print("SSQ: ", SSQ)
print("SQS: ", SQS)
print("diff: ", diff)
