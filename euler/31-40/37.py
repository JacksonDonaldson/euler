import math
def prime(n):
    if n<2:
        return False
    if n==2 or n==3 or n==5 or n==7:
        return True
    if n==4 or n==9:
        return False
        
    for i in range(2,math.ceil(n**.5)+1):
        if n%i==0:
            return False
    return True
trunc=[];
i=11;
while len(trunc)!=11:
    if prime(i):
        potential=True;
        for pos in range(1,len(str(i))):
            if not prime(int(str(i)[pos:])):
                potential =False;
                break
        if potential:
            for pos in range(0,len(str(i))):
                if not prime(int(str(i)[0:pos+1])):
                    potential =False;
                    break
        if potential:
            trunc.append(i);
    i+=2;
total=0;
for num in trunc:
    total+=num;
print(total);
