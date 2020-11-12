import mil
print(mil.m[0])
fractions = []
for i in range(0,12000):
    for j in range(0,i):
        good = True
        for base in mil.m[i]:
            if base in mil.m[j]:
                good = False
                break
        if good:
            fractions.append([j+1, i+1])
    if(i%1000 == 0):
        print(i)
sorter = fractions.copy()
for i in range(0, len(sorter)):
    sorter[i] = [sorter[i][0]/sorter[i][1], sorter[i]]
sorter.sort()
for i in range(0,len(sorter)):
    fractions[i] = sorter[i][1]
print(fractions.index([1,2]) - fractions.index([1,3])-1)
