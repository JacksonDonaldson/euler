f = open("81.txt")
text = f.read()
f.close()
tList = text.split("\n")
print(len(tList))
for i in range(0,len(tList)):
    tList[i] = tList[i].split(",")
for i in range(0,80):
    for j in range(0,80):
        tList[i][j] = int(tList[i][j])
        
        
tList.pop()
for i in range(1,80):
    tList[0][i] += tList[0][i-1]
    tList[i][0] += tList[i-1][0]
for i in range(1,80):
    for j in range(1,80):
        tList[i][j] += min(tList[i-1][j], tList[i][j-1])
        
print(tList[-1][-1])
