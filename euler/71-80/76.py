import math
from functools import cache

def combosLTEn(l, n):
    #use every int in l at least once
    pass

@cache
def waysToMake(n):
    #given n, find number of ways to sum to n that do not overlap with previous ones
    if n == 1:
        return set([tuple([1])])
    thisNum = [0] * n
    thisNum[n-1] = 1
    ways = set([tuple(thisNum)])
    
    for i in range(1,math.ceil(n/2)+1):
        combos = waysToMake(i)
        for other in waysToMake(n-i):
            for way in combos:
                t = list(way).copy()
                t.extend([0] * (n - len(t)))
                for i in range(0,len(other)):
                    t[i] += other[i]
                
                ways.add(tuple(t))
    return ways

def make(n):
    total = 0

@cache
def makeEx(n, ex):
    if n == 1:
        return 1
    if ex > n:
        return 0
    total = 1;
    for i in range(ex, int(n/2)+1):
        #print("calling make with " + str(n-i) +" and "+ str(i))
        total += makeEx(n-i, i)
    return total

for i in range(0,101,10):
    print(i)
    print(makeEx(i,1))
    
#not 190569292 (have to - 1)
    
