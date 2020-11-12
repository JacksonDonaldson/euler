import math
def form(n,a,b):
    return int((n**2)+(a*n)+b)
def isPrime(n):
    if n<=1:
        return False
    if n<=5:
        return True
    for j in range(2,math.ceil(n**(0.5))):
        if n%j==0:
            return False
    return True
maxi=0;
vals=[];
for a in range(-999,1000):
    for b in range(-1000, 1001):
        i=0;
        #print(form(i,a,b));
        while(isPrime(form(i,a,b))):
              i+=1;
        if i>maxi:
              maxi=i;
              vals=[a,b];
print(vals[0]*vals[1]);
