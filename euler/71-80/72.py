#essentially, sum from 0 to 1000000 of phi(i)
from sympy import factorint
import math
from functools import reduce
def getRemovalPattern(removals):
    pattern = [0] * reduce(math.lcm, removals)
    for num in removals:
        i = 1
        while num * i <= len(pattern):
            pattern[num * i-1] = 1
            i+=1
    return pattern
def findEliminated(n, prime, removals):
    #print(prime)
    #print(removals)
    potentials = int(n/prime - 1)
    #print("potential removals: " + str(potentials))
    if(removals):
        #not all of the numbers that could be eliminated by this prime count
        #because some of them have already been removed
        pattern = getRemovalPattern(removals)
        lPat = len(pattern)
        #print("pattern: " + str(pattern))
        noGood = potentials // lPat * sum(pattern)
        #print("pre no good: " + str(noGood))
        i = (potentials // lPat) * lPat *prime + prime#the first this many are checked, now manually check the final few
        while i < n:
            
            #print("checking " + str(i))
            for num in removals:
                if i % num == 0:
                    #print("covered")
                    noGood +=1
                    break
            i+=prime
            
        #print("nogood: " + str(noGood))
        potentials -=noGood
    #print("removed: " + str(potentials))
    return potentials
    
def phi(n):
    factors = list(set(factorint(n)))
    factors.sort()
    #given a list of factors of n, determine how many numbers less than n can be
    #represented as a multiple of those factors
    total = 0
    used = []
    
    for num in factors:
        total += findEliminated(n, num, used)
            
        used.append(num)
    
    
    return (n-1) - total

total = 0;
for i in range(2,1000001):
    total += phi(i)
    if(i % 10000 == 0):
        print(i)
print(total)
