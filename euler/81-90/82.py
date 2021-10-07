f = open("82.txt")
lines = [i.split(",") for i in f.read().split("\n")]
lines = lines[:-1]
for i in range(len(lines)):
    for j in range(len(lines)):
        lines[i][j] = int(lines[i][j])
for line in lines:
    print(line)
for c in range(1,len(lines)):
    #print(c)
    temp = []
    for i in range(len(lines)):
        temp.append(lines[i][c] + lines[i][c-1])

    while True:
        if(temp[1] + lines[0][c] < temp[0]):
            temp[0] = temp[1] + lines[0][c]
        if(temp[-2] + lines[-1][c] < temp[-1]):
            temp[-1] = temp[-2] + lines[-1][c]
        for i in range(1,len(lines) - 1):
            if temp[i-1] + lines[i][c] < temp[i]:
                #print("move found!")
                #print(lines[i][c])
                temp[i] = temp[i-1] + lines[i][c]
                break
            if temp[i+1] + lines[i][c] < temp[i]:
                #print("move foun")
                #print(lines[c][i])
                temp[i] = temp[i+1] + lines[i][c]
                break
        else:
            break
    for i in range(len(lines)):
        lines[i][c] = temp[i]

print(min([lines[i][-1] for i in range(len(lines))]))
