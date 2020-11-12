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
for i in range(1,30001):
    divs=finddivs(i);
    k=0;
    for num in divs:
        k+=num;
    k-=i;
    sums.append(k);
op=[];
for i in range(0,21823):
    if sums[i] >i+1:
        op.append(i+1);
print('options found');
for i in range(0,21823):
    can=False
    for option in op:
        if option>i:
            break
        if i-option in op[op.index(option):]:
            can=True;
            break
    if i%100==0:
        print(i);
    if not can:
        total+=i;
print(total);
