import math
i = 1181609232
while True:
    i+=1
    num = str(i * i)
    if len(num) != 19:
        continue
    if num[0] == '1' and num[2] == '2' and num[4] == '3' and num[6] == '4' and num[8] == '5' and num[10] == '6' and num[12] == '7' and num[14] == '8' and num[16] == '9' and num[18] == '0':
        print(i)
        quit()
