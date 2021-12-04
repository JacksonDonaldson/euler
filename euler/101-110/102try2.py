l = open("102.txt").read().split("\n")
l = [i.split(",") for i in l]
l=l[:-1]
for i in range(len(l)):
    l[i] = [int(j) for j in l[i]]

def findYIntercept(line, axis):
    if axis == 1:
        other = 0
    else:
        other = 1
    p1 = line[0]
    p2 = line[1]
    m = (p2[other]-p1[other])/(p2[axis]-p1[axis])
    return -1 * m * p1[axis] + p1[other]

def getValuesAt0(p1,p2,p3, axis):
    x=0
    lines = []
    if (p1[axis] < x and p2[axis] > x) or (p1[axis] > x and p2[axis] < x):
        lines.append([p1,p2])
    if (p1[axis] < x and p3[axis] > x) or (p1[axis] > x and p3[axis] < x):
        lines.append([p1,p3])
    if (p3[axis] < x and p2[axis] > x) or (p3[axis] > x and p2[axis] < x):
        lines.append([p3,p2])
    l1, l2 = lines
    if(len(lines) != 2):
        print("BAD")

    y1 = findYIntercept(l1,axis)
    y2 = findYIntercept(l2,axis)
    
    return [min(y1,y2),max(y1,y2)]

def containsOrigin(p1,p2,p3):
    mix = min([p1[0],p2[0],p3[0]])
    miy = min([p1[1],p2[1],p3[1]])
    maax = max([p1[0],p2[0],p3[0]])
    may = max([p1[1],p2[1],p3[1]])

    if mix > 0 or miy > 0:
        return False
    if maax < 0 or may < 0:
        return False

    x = getValuesAt0(p1,p2,p3,0)
    y = getValuesAt0(p1,p2,p3,1)
    return x[0] <= 0 and x[1] >= 0 and y[0] <=0 and y[1] >=0

total = 0
i=0
for tri in l:
    i+=1
    if i==431 or containsOrigin((tri[0],tri[1]),(tri[2],tri[3]),(tri[4],tri[5])):
        total += 1
        print(i)
print(total)
