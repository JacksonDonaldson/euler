import math
b = 1
while True:
    if (math.sqrt(1+2*(b**2-b))) % 2 == 1:
        if(math.sqrt(1+2*(b**2-b)) ** 2 == 1+2*(b**2-b)):
            print(b)
    b+=1
print((1+(1+2*(b**2-b))**.5) /2)
math.sqrt(1+2*(b**2-b))
