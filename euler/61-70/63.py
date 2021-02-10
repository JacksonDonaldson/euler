import math
total = 0
for i in range(1,2000):
    j = 1;
    toTest = math.pow(j,i)
    while int(math.log10(toTest)) + 1 <= i:
        if int(math.log10(toTest)) + 1 == i:
            total += 1
            print(str(toTest))
            print(i)
            print(j)
        j+=1
        toTest = math.pow(j,i)
print(total)
#not 9, 34
