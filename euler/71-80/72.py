import prime
import pfact
factors = [1]
for i in range(2,1000001):
    factors.append(pfact.factor(i))
    if i %10000 == 0:
        print(i)
file = open("million.txt", 'w+')
file.write(factors)
f.close()
k =10000
for d in range(2,k+1):
    if prime.p(d):
        total += d-1
        continue
    goodList = [False]
    for i in range(1,d-1):
        goodList.append(None);
    #print(d)
    for i in range(0,len(goodList)):
        if goodList[i] == None:
            #print('dividing ' + str(d) + ' by ' + str(i+1))
            if d % (i+1) == 0:
                isDivisable = True
            else:
                isDivisable = False
            j = i;
            #print(isDivisable)
            while j < len(goodList):
                if goodList[j] != True:
                    goodList[j] = isDivisable
                j+=(i+1)
    #print(goodList)
    for boo in goodList:
        if not boo:
            total+=1;
##    for n in range(1,d):
##        nFact = pfact.factor(n);
##        good = True
##        for fact in nFact:
##            if d%fact == 0:
##                good = False
##                break
##        if good:
##            total+=1;
    if d%100 == 0:
        print(d)
print(total/k**2)
