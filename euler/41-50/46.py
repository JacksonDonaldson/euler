import math
def prime(n):
    if n<2:
        return False
    if n <4:
        return True
    for i in range(2,math.ceil(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
primes =[]
for i in range(1,1000000):
    if prime(i):
        primes.append(i);
print('primed')
i=3
while True:
    i+=2
    if i in primes:
       continue
    for prime in primes:
        if prime>i:
            print("found");
            print(i);
        if math.sqrt((i-prime)/2) %1 == 0:
            if(i%10000 == 0):
                print(str(i) + 'no good')
            break
        
