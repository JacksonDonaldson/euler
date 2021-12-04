def findLineSquare(p1, p2):
    return pow((p1[0] - p2[0]),2) + pow(p1[1] - p2[1], 2)
def isRightTriangle(p1,p2,p3):
    #find the 3 line lengths
    l1 = findLineSquare(p1,p2)
    l2 = findLineSquare(p2,p3)
    l3 = findLineSquare(p1,p3)

    hyp = max([l1,l2,l3])
    s1 = min([l1,l2,l3])
    s2 = sum([l1,l2,l3]) - hyp - s1

    return hyp == s1 + s2

d = 51
total = 0
points = []

for x in range(d):
    for y in range(d):
        if x == y == 0:
            continue
        points.append((x,y))

for i in range(len(points) - 1):
    for point in points[i+1:]:
        
        if(isRightTriangle((0,0),points[i],point)):
                total +=1
                #print(f"p1: {points[i]} p2: {point}")
    #print(f"point done. {total}")

print(total)
#not 13611
