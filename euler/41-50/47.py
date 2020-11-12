import prime
primes =[];
for i in range(2,1000000):
    if prime.p(i):
        primes.append(i)
i=1;
print("primed")
run = 0;
while run !=4:
    i+=1;
    test = i;
    pfacts = [];
    while test !=1:
        j=0;
        while True:
            if test%primes[j] == 0:
                pfacts.append(primes[j])
                test=test/primes[j]
                break
            j+=1;
    unique = [];
    for pfact in pfacts:
        if pfact not in unique:
            unique.append(pfact)
    if len(unique) == 4:
        run+=1
    else:
        run = 0
print(i-3);
