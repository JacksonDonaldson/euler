import math
def prime(n):
    for i in range(2,math.ceil(n**.5)+1):
        if n%i==0:
            return False
    return True
primes=[2];
for i in range(3,1000000):
    if prime(i):
        primes.append(i);
print('primed');
total=0;
for prime in primes:
    circular=True
    for i in range(0,len(str(prime))):
        #print(prime);
        prime=str(prime)[1:]+str(prime)[0];
        if int(prime) not in primes:
            circular=False;
            break
    if circular:
        print(prime);
        total+=1;
print(total);
