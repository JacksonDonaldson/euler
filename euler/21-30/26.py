import math
base =2;
result=[];
maxrepeat=0;
maxpoint=0;
for i in range(1,1001):
    result=[];
    top=1;
    stor=[];
    while top!=0:
        #print(top);
        #print(result);
        if top in stor:
            print('repeat');
            if len(stor)-stor.index(top)>maxrepeat:
                maxrepeat=len(stor)-stor.index(top);
                maxpoint = i;
            break
        stor.append(top);
        result.append(math.floor(top/i));
        
        top=(top%i)*10
    #print(result);
print(maxpoint);
