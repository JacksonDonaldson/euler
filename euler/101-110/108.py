import pfact
from sympy import isprime
from functools import cache
import random

def findNumSol(n):
    total = 0
    for y in range(n+1, 2*n+1):
        if ((n * y) / (y-n)).is_integer():
            total+=1
    return total

def findNumSol(n):
    total = 0
    nSq = n *n
    for a in range(1, n+1):
        if nSq % a == 0:
            total += 1
    return total

@cache
def primeList(n):
    if n == 0:
        return 2
    i = 0
    p = 3
    while i < n:
        if isprime(p):
            i+=1
        p+=1
    return p-1

def findThing(values):
    values = values.copy()
    #mult = [2,3,5,7,11,13,17,19]
    values.sort()
    values.reverse()
    if values[0] == 1:
        return 1 + sum([pow(3,i) for i in range(len(values))])
    additive = 1
    for add in values[1:]:
        additive *= primeList(add)
    values[0]-=1
    return additive + findThing(values)

def findOptimalAddSpot(l):
    init = findThing(l.copy())
    options = []
    for i in range(len(l)):
        l2 = l.copy()
        l2[i] += 1
        delta = findThing(l2) - init
        options.append(delta / primeList(i))

    for i in range(len(l)):
        l2 = l.copy()
        l2[i] += 2
        delta = findThing(l2) - init
        options.append(delta / primeList(i) ** 2)

    
    m = max(options)
    l2 = l.copy()
    l2.append(1)
    if m > findThing(l2) / primeList(len(l)):
        print(l[options.index(m)])
        l[options.index(m) % len(l)] += 1 * ((options.index(m) // len(l)) + 1)
        
        print(l[options.index(m)])
    else:
        l.append(1)

        
l = [1]
while findThing(l.copy()) < 4000000:
    findOptimalAddSpot(l)

def foo(l):
    total = 1
    
    for i in range(len(l)):
        
        total *= primeList(i) ** l[i]

    return total
print(foo(l))

def findByRand(l):
    while True:
        l2 = l.copy()

        if(random.randint(1,5) == 1):
            l2.append(1)
        elif random.randint(1,5) == 1:
            l2.pop(len(l2) - 1)
        elif(random.randint(1,5) == 1):
            l2.append(1)
        indexCount = random.randint(1,len(l2))
        
        
        for i in range(indexCount):
            index = random.randint(0,len(l2)-1)
            l2[index] += random.randint(-2,9)
            if l2[index] < 1:
                l2[index] = 1
        if(findThing(l2) > 4000000 and foo(l2) < foo(l)):
            print(foo(l2))
            l = l2
            print(l)
            
def please(l):
    while findThing(l) < 4000000:
        l.append(1)
    return foo(l)<= 8014397185594800
    
#ans < 6258862563988320

##
##i = 0
##m = 0
##while m < 1000:
##    if findNumSol(i) > m:
##        m = findNumSol(i)
##        print(f"i: {i}, max: {m}")
##        print(pfact.primeFact(i))
##    #print(f"i: {i}, nums: {findNumSol(i)}")
##    i+=1
##print(i)

#165894 < ans < 180180


