# print all the prime numbers in an interval

def checkPrime(num:int)->bool:
    if num < 0:
        return False
    flag = 0
    for i in range(1, int(num/2)+1):
        if (num % i) == 0:
            flag += 1
    if flag != 1:
        return False
    return True

for i in range(1, 100):
    if checkPrime(i):
        print(i, end=",")
    continue