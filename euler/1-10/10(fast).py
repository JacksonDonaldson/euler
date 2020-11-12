allNum = [];
i = 2;
while i<2000000:
    allNum.append(i);
    i+=1;
i = 0;
while True:
    pops = [];
    append = pops.append
    i = 0;
    nums = len(allNum);
    i2=0;
    while i2<nums:
        if allNum[i2]%allNum[i] == 0:
            append(i);
        i2+=1;
    i2 = 1;
    print('popping');
    while i2<len(pops)+1:
        allNum.pop(pops[-1*i2]);
        i2+=1;
    pops.clear();
    print('done');
    if allNum[i] >= 1999999:
        break
    i+=1;
i = 0;
total = 0;
while i<len(allNum):
    total +=allNum[i];
    i+=1;
print(total);
    

    
    
    
