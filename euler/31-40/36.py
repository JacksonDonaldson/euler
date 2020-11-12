import basecount
import math
def palcheck(num):
    for i in range(0,math.floor(len(num)/2)):
        if num[i]!=num[-i-1]:
            return False
    return True
base10 =[0]
base2=[0];
total=[];
for i in range(1,1000000):
    #print(i);
    #print(base10);
    #print(base2);
    base10 = basecount.ct(10,base10);
    base2 = basecount.ct(2,base2);
    if palcheck(base10) and palcheck(base2):
        total.append(tuple(base10));
    
#print(total);
actualtotal=0;
for num in total:
    temp='';
    for digit in num:
        temp+=str(digit);
    actualtotal+=int(temp);
print(actualtotal);
