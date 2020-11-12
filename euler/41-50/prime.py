import math
def p(n):
    if n<2:
        return False
    if n ==2 or n==3 or n==5 or n==7:
        return True
    for i in range(2,math.ceil(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
