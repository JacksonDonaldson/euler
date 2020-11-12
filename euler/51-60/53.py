import math
def test(n,r):
    if math.factorial(n)/(math.factorial(r)*math.factorial(n-r)) > 1000000:
        return True
    return False
total = 0;
for i in range(1,101):
    for j in range(1,i):
        if test(i,j):
            total+=1;
print(total)
