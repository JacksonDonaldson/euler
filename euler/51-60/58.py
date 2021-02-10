import math
def prime(n):
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
sideLen = 2
primes = 3
currentNum = 9
diagonalTotal = 4
while primes/diagonalTotal > 8/13:
    sideLen +=2
    for i in range(4):
        currentNum += sideLen
        #print(currentNum)
        if prime(currentNum):
            #print("Prime!")
            primes +=1
        diagonalTotal +=1

print(sideLen - 1)
#sideLen != 26240 or 42 or 44 or 43 or 45
