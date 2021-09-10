import math
import time
import cProfile
import pstats

def findX(d):
    x = 1
    found = False
    while not found:
        x+=1
        
        if pow(x,2,d) == 1:
            v= x * x
            last = v % 10
            if last in [2,3,7,8]:
               continue
##            s = sum(map(int,str(x)))
##            while s > 10:
##                s = sum(map(int,str(s)))
##            if s in [2,3,6,8]:
##                continue
            if math.sqrt((v-1)/d).is_integer():
                found = True
    return x
t= time.time()
def isSquare(n):
    return math.sqrt(n).is_integer()
def findXbyY(d):
    y = 1
    done = False
    while not done:
        
        y+=1
        
        n = (d * y * y) + 1
        if(isSquare(n)):
            done = True
        i=0
        while not isSquare(n+i):
            i+=1
        print(str(n) + ": off " + str(i) +" from " + str(math.sqrt(n+i)) + "(" + str(n+i) + ")")

def additiveTest(d):
    y = 2
    yVal = d + 1
    xVal = 1
    x = 2
    while xVal != yVal:
        if xVal<yVal:
            xVal += 2 * x - 1
            x+=1
        else:
            yVal += d*(2 * y - 1)
            y+=1
    return x - 1
    
##with cProfile.Profile() as pr:
##    findX(61)
##stats = pstats.Stats(pr)
##stats.sort_stats(pstats.SortKey.TIME)
##stats.print_stats()
m = 0
for i in range(2,1001):
    if math.sqrt(i).is_integer():
        continue
    x = additiveTest(i)
    print("i: " + str(i) + " x: " + str(x))
    if x > m:
        
        m = x
        print("M: " + str(m))
##    
##print(time.time() - t)
#not 973

    

