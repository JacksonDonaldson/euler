import basecount;
ones = [0,3,3,5,4,4,3,5,5,4];
#0-9
teens= [3,6,6,8,8,7,7,9,8,8];
#10-19
tens = [0,0,6,6,5,5,5,7,6,6];
#0-90
def findtens(ten,one):
    if ten==0:
        return ones[one];
    if ten ==1:
        return teens[one];
    else:
        return tens[ten]+ones[one];
    
def findlen(hundred, ten, one):
    if ten==0 and one==0:
        return ones[hundred]+7;
    if hundred==0:
        return findtens(ten,one)
    return ones[hundred]+10+findtens(ten,one)
index = [0,0,0];
total=0;
for i in range(0,1000):
    index = basecount.ct(10,index);
    print(index);
    if len(index)==3:
        test=total;
        total += findlen(index[0],index[1],index[2]);
        print(total-test);
    else:
        print('hey');
        total+=11;
print(total);
