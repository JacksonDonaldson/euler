import math
total=0;
sums=[];
def finddivs(i):
    div =[];
    for j in range(1,math.floor(i**.5)+1):
        if i%j==0:
            if j not in div:
                div.append(j);
            if i/j not in div:
                div.append(i/j);
    return div;
for i in range(1,30000):
    divs=finddivs(i);
    k=0;
    for num in divs:
        k+=num;
    k-=i;
    sums.append(k);
for i in range(0,10000):
    if sums[int(sums[i])-1]==i+1:
        if sums[i]!=i+1:
            total+=i+1;
        print(i+1);
print(total);
        
