def findPerms(values):
    if len(values) == 1:
        return values;
    perms = findPerms(values[0:-1])
    toReturn = []
    for perm in perms:
        i = 0;
        while i< len(perm)+1:
            toReturn.append(perm[:i] + values[-1] + perm[i:])
            i+=1
    return toReturn
            
import prime
primes = []
for i in range(1000,10000):
    if prime.p(i):
        primes.append(i)
for prime in primes:
    primePerms = [];
    tests = findPerms([str(prime)[0], str(prime)[1], str(prime)[2], str(prime)[3]])
    
    for test in tests:
        if int(test) in primes and test not in primePerms:
            primePerms.append(test);
    primePerms.sort();
    if prime == 2969:
        print(primePerms)
    if len(primePerms) >2:
        for prime1 in primePerms:
            if prime1 == prime:
                continue
            if str(int(prime) + 2 * (int(prime1) - int(prime))) in primePerms:
                print('subs')
                print(primePerms[0]);
                print(prime)
