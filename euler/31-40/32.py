import math
def findfactors(n):
    factors=[];
    for i in range(1,math.ceil(n**.5)):
        if n%i==0:
            if [[i,n/i]] not in factors:
                factors.append([i,int(n/i)]);
    return factors
total=0;
for i in range(2,10000):
    factors= findfactors(i);
    for factor in factors:
        if len(str(factor[0]))+len(str(factor[1]))+len(str(i))==9:
            donenum=[];
            for num in str(factor[0])+str(factor[1])+str(i):
                if num in donenum:
                    break
                if num=='0':
                    break
                else:
                    donenum.append(num);
            if len(donenum)==9:
                total+=i;
                print(i);
                print(factor);
                break
print(total);
