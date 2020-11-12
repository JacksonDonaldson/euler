import pfact;


total = 0;
ar = [];
i = 0;
while True:
    i+=1;
    total+=i;
    #if total < 3603600:
    #    continue

    #check divisors
    
    divisors = 0;
    primes = pfact.factor(total);
    #print(primes);
    mults = [];
    do = True;
    for prime in primes:
        do = True;
        #print(mults);
        for mult in mults:
            if mult[0] == prime:
                index = mults.index(mult);
                mults[index] = [prime,mults[index][1]+1];
                do = False;
        if do:
            mults.append([prime,1]);
            
    divisors = 1;
    #print(mults);
    for mult in mults:
        divisors = divisors*(mult[1]+1);
    #print(total);
    #print(divisors);
    if divisors >= 500:
        print(total);
        break
    
        
