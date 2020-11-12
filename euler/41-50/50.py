i = 3;
import prime
primes=[2,3]
while True:
    i+=1;
    if prime.p(i):
        primes.append(i);
    if primes[-1] + primes[-2] > 1000000:
        break
maxPrime = 0;
print('primed')
i=0;
maxIndex = 0;
for i in range(0,len(primes)):
    total = primes[i];
    index = 1;
    while total < 1000000:
        if index>maxIndex:
            if prime.p(total):
                maxIndex = index
                maxPrime = total
                print(maxPrime)
        total = total + primes[i+index]
        
        index +=1;
    i+=1
    #if i %100 == 0:
        #print(i)
print(maxTotal);
