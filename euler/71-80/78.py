import math
from functools import cache
import csv

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

i = 0
last = 0
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
def printRep():
    for i in range(1,100):
        l = [0] * i
        w = waysToMake(i)
        for j in range(i):
            l[j]= sum([1 for k in w if k[j] != 0])
            w = [k for k in w if k[j] == 0]
        print(l)


def getIthSumForPos(ar, pos,i):
    return sum(ar[pos][i-1:])
    
    
    
nums = [[1],[1,1],[2,0,1]]

def get(nums, n):
    total = []
    for j in range(1,int(n/2)+1):
        total.append(getIthSumForPos(nums, n,j))
    return total

i = 5
while True:
    nums.append(get(nums, i))
    i+=1
    print(i)
    
        

    
    
    
