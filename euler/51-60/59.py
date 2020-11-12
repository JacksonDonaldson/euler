f = open("59.txt")
values = f.read()
firstValue = -1
listed = []
i = 0
for value in values:
    if value == ",":
        listed.append(int(values[firstValue+1:i]))
        firstValue = i
    i+=1
listed.append(94)
def xor(i, j):
    i = bin(i)[2:]
    j = bin(j)[2:]
    while len(i)<8:
        i = '0' + i
    while len(j) < 8:
        j = '0' + j
    result = ''
    for k in range(0,8):
        if(i[k] == j[k]):
            result += "0"
        else:
            result += "1"
    return int(result, 2)
leng = len(listed)
for a in range(101,123):
    for b in range(120,123):
        for c in range(112,123):
            i = 0
            xord = []
            for to in listed:
                if i == 0:
                    xord.append(xor(a,to))
                elif i == 1:
                    xord.append(xor(b,to))
                else:
                    xord.append(xor(c,to))
                #print(xord[-1])
                if xord[-1]<32:
                    print("broken")
                    break
                i+=1
                i = i%3
                
            if len(xord) == leng:
##                print(a)
##                print(b)
##                print(c)
##                print(xord)
                for l in range(0,len(xord)):
                   if xord[l] == 116 and xord[l+1] == 104 and xord[l+2] == 101 and xord[l+3] == 32:
                        print(a)
                        print(b)
                        print(c)
                        total = 0
                        for char in xord:
                            total += char
                            print(chr(char), end = '')
                        print(total)
                        print(xord)
               
               
                
    print('ayyy')
