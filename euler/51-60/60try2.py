import math
from functools import cache
def prime(n):
    for i in range(2,math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def getNextPrime(start):
    i = start
    while True:
        if prime(i):
            yield i
        i+=1

def primeList(n):
    l = []
    i=2
    while len(l)<n:
        if prime(i):
            l.append(i)
        i+=1
    return l

@cache
def reversable(p1, p2):
    return prime(int(str(p1) + str(p2))) and prime(int(str(p2) + str(p1)))

def allReversable(known, extra):
    for k in known:
        if not reversable(k, extra):
            return False
    return True
def getValidPrimes(pr):
    p = getNextPrime(pr+1)
    t = next(p)
    l=[]
    while t < 9999:
        if(reversable(pr,t)):
            l.append(t)
        t = next(p)
    return l
pLinks = {}
plist = getNextPrime(3)
##for pr in plist:
##    pLinks[pr] = getValidPrimes(pr)
##    if pr > 1000:
##        break

#idea: links
pList = primeList(9999)
def findMin(known,last, currentMin):
    global pList
    #recursively search for the minimum way to combine 5 primes such that all are concatable primes
    #Given that known is all the primes we have up to this point, and that last was the last prime added (and also the largest)
    #we continue searching for the smallest value possible to add to known from last.
    #once we find a prime value that works with all the given in known, find the min result from that number
    #Continue searching primes until we pass the point where adding a new prime already exceeds the min we got from the last number, then return our min
    #print(known)
    currentSum = sum(known)
    if currentSum > currentMin:
        return currentMin
    if len(known) == 5:
        return sum(known)

    
    
    
    nextValue = last + 1
    minFound = currentMin
    #print(minFound)
    for p in pList[last:]:
        #print("looping")
        if currentSum + p > minFound:
            return minFound
        
        if allReversable(known, p):
            value = findMin(known+[p], pList.index(p), minFound)
            if value < minFound:
                minFound = value
                print("found new min of " + str(minFound))
                print("known: " + str(known))
    return minFound
                
#ans = 26033
