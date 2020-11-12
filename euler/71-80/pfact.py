primes = []
import prime
for i in range(1,1000000):
    if prime.p(i):
        primes.append(i);
print('primed')
def factor(num):
    factors = [];
    i = 0;
    while num !=1:
        if num % primes[i] == 0:
            factors.append(primes[i]);
            num = num/primes[i];
            i = -1;
        i+=1;
    return factors
