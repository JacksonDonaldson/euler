stor = 1;
i = 0;
tempmoves = [];
tempposition = [];
nums=[];
while i<120000000:
    nums.append('');
    i+=1;
print('done');
most = 0;
mostnum = 0;
while stor<1000000:
    test = stor;
    moves = 0;
    while test!=1:
        if test<120000000:
            if nums[int(test)]!='':
                moves+=nums[int(test)];
                test=1;
                continue
            else:
                tempposition.append(test);
                tempmoves.append(moves);
        if test %2 == 0:
            #print('div');
            test = test/2;
        else:
            test = (test*3)+1;
        moves+=1;
        #print(moves);
        
        
    i = 0;
    while i<len(tempposition):
        nums[int(tempposition[i])] = moves-tempmoves[i];
        i+=1;
    tempmoves.clear();
    tempposition.clear();
    if moves>most:
        most = moves;
        mostnum = stor;
    stor+=1;
    if stor%1000 == 0:
        print(stor);
print(mostnum);
    
                    
