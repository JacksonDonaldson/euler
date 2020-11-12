total = 2;
test = 3;
primes = [2,3]
imp = 0;
while test<2000000:
    i = 2;
    prime = True;
    while i<len(primes):
        if test%primes[i] == 0:
            prime = False;
            break
        if primes[i]>(test**(1/2)):
            break
        i+=1
    if prime:
        if test-imp >10000:
            print(test);
            imp= test;
        primes.append(test);
        #print(test);
        total += test;
    test+=2;
print(total);
