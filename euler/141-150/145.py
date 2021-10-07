reversable = 0
for i in range(1,1000000000):
    if(i%1000000 == 0):
        print(i)
    j = str(i)
    if j[-1] == "0":
        continue
    j = j[::-1]
    i+=int(j)
    i = str(i)
    for o in ["0","2","4","6","8"]:
        if o in i:
            break
    else:
        reversable+=1

print(reversable)
