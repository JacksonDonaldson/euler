import math
def digitFact(i):
    return sum([math.factorial(int(c)) for c in str(i)])
sixtyCount = 0
for i in range(10,1000000):
    if(i % 100000 == 0):
        print(i)
    j = 1
    #print("i: " + str(i))

    while i not in [145,169,363601,1454,871,45361,872,45362]:
        prevI = i
        i = digitFact(i)
        if i == prevI:
            break
        j+=1
    if i in [169,363601,1454]:
        j+=2
    elif i in [871,45361,872,45363]:
        j+=1
    
    #print("j: " + str(j))
    if j == 60:
        sixtyCount +=1
        print("count + 1!")
print(sixtyCount)
