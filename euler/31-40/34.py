bigtotal=0;
factorial=[1,1,2,6,24,120,720,5040,40320,362880]
def fact(n):
    return factorial[n];
for i in range(3,10000000):
    total=0;
    for letter in str(i):
        total+=fact(int(letter));
    if i%1000000 ==0:
        print(i);
    if total==i:
        print(i);
        bigtotal+=i;
