total = 0
def reverse(i):
    return int(str(i)[::-1])
def palendrome(i):
    i = str(i)
    length = int(len(i)/2)
    for j in range(0,length):
        if i[j] != i[-(j+1)]:
            return False
    return True
for i in range(10,10000):
    n = 0
    lychrel = True
    while n < 50:
        i += reverse(i)
        if(palendrome(i)):
            lychrel = False
            break
        n+=1
    if(lychrel):
        total+=1
    #print(i)
print(total)
