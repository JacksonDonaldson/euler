stor=0;
biggest=0;
import math
for a in range(1,1000):
    atotal=0;
    for b in range(1,a):
        for c in range(1,a):
            first=(b**2);
            second=(c**2);
            third=((b**2)+(c**2))**.5;
            if (first+second+third)%1 ==float(0):
                if float(b+c+third) ==float(a):
                   atotal+=1;
    if atotal>biggest:
        biggest=atotal;
        stor=a;
    print(a);
print(biggest);
print(stor);
