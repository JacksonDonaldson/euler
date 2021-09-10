f = open("99.txt")
import math
pairs = []
i = f.readline()
while "\n" in i:
    pairs.append([int(i[0:i.index(",")]),int(i[i.index(",")+1:i.index("\n")])])
    i = f.readline()
pairs.append([int(i[0:i.index(",")]),int(i[i.index(",")+1:])])

mV = pairs[171][0] ** pairs[171][1]
mVn = pairs[171][0]
mVx = pairs[171][1]

lineNum = 171
def larger(n1, x1, n2, x2, v2):
    divisor = math.gcd(x1,x2)
    n1 = n1 ** int(x1/divisor)
    if(divisor > 1):
        #print("this is useful!")
        n2 = n2 ** int(x2/divisor)
    else:
        n2 = v2
        
    return n1 > n2 
for i in range(544,1001):
    if larger(pairs[i][0], pairs[i][1], mVn, mVx, mV):
        mV = pairs[i][0] ** pairs[i][1]
        mVn = pairs[i][0]
        mVx = pairs[i][1]
        lineNum = i
        print("linenum: " + str(lineNum))
#not 171, 708, 707
#it is 709

#171 max up to 545
