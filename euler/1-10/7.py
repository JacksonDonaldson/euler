count = 2;
num = 2;
i = 1;
while i < 10001:
    num = count;
    primes = [];
    i2 = 2;
    fail = num/2;
    while num !=1:
        
        if num % i2 == 0:
            primes.append(i2);
            num = num/i2;
            i2 = 1;
        if i2>fail:
            primes.append(num);
            num = 1;
            
        i2+=1;
    
    count+=1;
    if len(primes) == 1:
        i+=1;
        if i%75 ==  0:
            print(i);
    
    
