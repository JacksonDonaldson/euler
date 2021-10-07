#final point must be between the origin, a line extended from p1 to the origin, and a line extended from p2 to the origin.
def sign(n):
    if n == 0:
        return 0
    return n / abs(n)
def otherSide(x,y,m,otherX,otherY):
    if m == "v":
        return otherX == 0 or x/otherX<0
    if m == 0:
        return otherY/y < 0
    if(x * m) > y:
        return otherX * m <= otherY
    return otherX * m >= otherY

def between(x,y,m1,m2):
    if m1 =="v":
        if m2=="v":
            return True
        return y >= x*m2
    if m2 == "v":
        return y <= x *m1
    ma = max(x*m1,x*m2)
    m = min(x*m1,x*m2)
    return y <= m or y >=ma
def originInTriangle(x1,y1,x2,y2,x3,y3):
    if x1 == 0 and y1 == 0:
        return True
    if x2 == 0 and y2 == 0:
        return True
    if x3 == 0 and y3 == 0:
        return True

    if sign(x1) == sign(x2) == sign(x3):
        
        return False
    if sign(y1) == sign(y2) == sign(y3):
        return False
    
    if sign(x1) == sign(x2):
        odd = x3
        oddY = y3
    elif sign(x1) == sign(x3):
        odd = x2
        oddY = y2
        x2 = x3
        y2=x3
    elif sign(x2) == sign(x3):
        odd = x1
        oddY= y1
        x1 = x3
        x1=y3
    else:
        print("AAAAHHH")

    #y-y1=m(x-x1)
    #y=mx-mx1+y1
    #b=(-mx1+y1)
    #so, there are 2 nums, x1 and x2 that have the same sign
    #next, find the line drawn between them and the origin to know the constraints for the final value
    
    m1 = (y1-oddY)/(x1-odd)
    m2 = (y2-oddY)/(x2-odd)
    #print(m1)
    #print(m2)
    b1 = -m1 * x1 + y1
    b2 = -m2*x2 + y2
    #print(b1)
    #print(b2)
    return sign(b1) != sign(b2)

    minY = min(m1*odd,m2*odd)
    maxY = max(m1*odd,m2*odd)
    return minY<oddY<maxY
    



    
##    if x1 == 0 and y1 == 0:
##        return True
##    if x2 == 0 and y2 == 0:
##        return True
##    if x3 == 0 and y3 == 0:
##        return True
##    if y1 == 0 and y2 == 0:
##        return True
##    if(x1 == 0):
##        m1 = "v"
##    else:
##        m1 = y1/x1
##    if(x2 == 0):
##        m2 = "v"
##    else:
##        m2 = y2/x2
##
##    if(x1-x2 == 0):
##        sideM = "v"
##    else:
##        sideM = (y1-y2)/(x1-x2)
##        
##    if(not otherSide(x1,y1,sideM,x3,y3)):
##        print("on the same side")
##        return False
##    return between(x3,y3,m1,m2)

f = open("102.txt")
total = 0
other = 0
while f.readable():
    n = f.readline().split(",")
    if n[0] == "":
        break
    n = [int(i) for i in n]
    
    if(originInTriangle(n[0],n[1],n[2],n[3],n[4],n[5])):
        print(n)
        total += 1
    else:
        other +=1
        
print(total)
#not 325, 210, 205
