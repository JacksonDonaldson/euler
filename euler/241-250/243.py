import math
from functools import cache

def prime(n):
    if n == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

@cache
def pFact(n):
    fact = []
    while n != 1:
        i = 0
        while n % primes[i] != 0:
            i +=1
        n/=primes[i]
        fact.append(primes[i])
    return fact

def simplifiable(n,d):
    nFact = pFact(n)
    dFact = pFact(d)
    for n in nFact:
        if n in dFact:
            return True
    return False

def cancellable(n, dFact):
    while n != 1:
        i = 0
        while n % primes[i] != 0:
            i +=1
        if primes[i] in dFact:
            return True
        n /=primes[i]
    return False
def r(d):
    res = 1
    dFact = pFact(d)
    
    for i in range(2,d):
        if not cancellable(i, dFact):
            res+=1
    return res


primes = []
for i in range(2,1000000):
    if prime(i):
        primes.append(i)


print("primed")
minRes = 1
value = 0
i = 4
while True:
    i+=1
    if r(i) / (i-1) < minRes:
        minRes = r(i) / (i-1)
        value = i
        print(value)
        print(minRes)
    if minRes < 15499/94744:
        print(value)
        print("!!!!!!!!!!!!!!")
