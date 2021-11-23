import math
def primeFact(num):
    primes = []
    while num %2 == 0:
        primes.append(2)
        num /=2

    for i in range(3,int(math.sqrt(num)) + 1, 2):
        while ( num % i == 0):
            num /= i
            primes.append(i)

    if num != 1:
        primes.append(num)

    return primes
