import math
import prime
from functools import cache
#import pfact
#find minimal form and multiply out is the play
def getC(a,b):
    return math.sqrt(a**2+b**2)

def coprime(n,m):
    for l in pfact.factor(n):
        if l in pfact.factor(m):
            return False
    return True
def getMinimalPythagTrip(p, largest):
    #for some prime p as a, find all b values that result in a new workable pythagorean triple
    #a b value is new only if p and that value are coprime
    
    #starting at p**2, you can find the next potential c by adding 2i + 1, where i is the position of the square.
    #if the sum of the 2i+1s is a square at this point, that is a valid b
    a = p
    i=p
    total = 0
    b = []
    c=[]
    pSquared = p ** 2

    #finding the total distance to the next square
    while total < pSquared:
        total += 2*i+1
        i+=1
    
    
    lastB = 0
    lastC = i
    #keep increasing total, the distance to the next square, until we find an increase that is itself a perfect square
    while a + lastB + lastC < largest:
        lastB = math.sqrt(total)
        lastC = i + 1
        if(lastB.is_integer()):
            #there is a potential new value. Check it to see if it's coprime with a.
            if coprime(p,lastB):
                
                b.append(lastB)
        total += 2 * i + 1
        i +=1
    return b

#20,21,and 29 are a triple
#but is there any other possible triple for a,b,c where b > a?
#the sum from x=0 to x=k of (2(n+x)
#9-1/2+1= 5. 25 is the total.
#6,8,10: 
#sum from x = 0 to x = 0 of (n+x-1)/2
#but could also do sum from x = 0 to x = k of (n+x-1)/2 for any values of n and k.
#20,21,29 works but so does 20,99,101

#given p^2, it must break down into something like 2n+1, or (2n+1)+2(n+1)+1, and so on
#which resolves down into (2n)+2(n+1)+2(n+2)+x
#so for some value of x, p^2 must be 2*x*n + 2*sum(1,2,..x) + x
#given p = 400, what values of x can be used to produce a valid n?
ar = [0] * 1500001

@cache
def getXSum(x):
    return x + 2*(sum(range(1,x)))
                  
def xTest(p):
    global ar
    dif = p ** 2
    for x in range(int(p/2)+1,0,-1):
        if((dif - getXSum(x)) % (2 * x) == 0):
            b = (dif - getXSum(x)) / (2 * x)
            #print("x:"+ str(x) + " a: " + str(p) + " b: " + str(b) + " c: " + str(getC(p,b)))
            c = getC(p,b)
            t=int(p+b+c)
            if t > 1500000:
                break
            ar[t]=1
                
i = 2
while True:
    if i % 1000 == 0:
        print(i)
        print(sum(ar))
    xTest(i)
    i +=1

#up to a of 96k, there are 338188 values

        
