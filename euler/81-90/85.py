def fits(smallX,smallY,bigX,bigY):
    xPositions = (bigX - smallX)+1
    yPositions = (bigY - smallY)+1
    return xPositions * yPositions

def rectCount(x,y):
    total = 0
    for yDim in range(1,y+1):
        for xDim in range(1,x+1):
            total += fits(xDim,yDim,x,y)
    return total

closest = 111111111110
for x in range(1,100):
    for y in range(1,100):
        if abs(rectCount(x,y)-2000000) < closest:
            closest = abs(rectCount(x,y)-2000000)
            print(x,y)
