i = 1
def toList(n):
    lis = []
    for num in str(n):
        lis.append(num);
    lis.sort();
    return lis
while True:
    i+=1;
    first = toList(i)
    for j in range(1,7):
        if not toList(i*j) == first:
            break
        if j == 6:
            print(i)
            quit()
