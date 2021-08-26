#looking for highly composite numbers
#few relative primes.
from sympy import factorint
def findFacts(n):
    facts = []
    while n > 1:
        i = 2
        while True:
            if n % i == 0:
                n/=i
                facts.append(i)
                break
            i+=1
    return set(facts)
def phi(n):
    factors = set(factorint(n))
    #given a list of factors of n, determine how many numbers less than n can be
    #represented as a multiple of those factors
    total = 0
    used = []
    
    for num in factors:
        total += (n/num) - 1
        toRemove = set()
        for i in used:
            j = 1
            
            while (num * (i*j)) < n:
                
                toRemove.add(num * i * j)
                   
                j+=1
        total -= len(toRemove)
            
        used.append(num)
    
    
    return (n-1) - total

maxValue = 0
largest = 0
for i in range(2, 1000000):
    #factorint(i)
    if i / phi(i) > maxValue:
        maxValue = i/phi(i)
        largest = i
    if(i %1000 == 0):
        print(i)
print(maxValue)
print(largest)
