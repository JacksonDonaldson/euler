def factor(num):
    primes = [];
    i = 2;
    while num !=1:
        if num % i == 0:
            primes.append(i);
            num = num/i;
            i = 1;
        i+=1;
    return primes
