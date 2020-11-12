i=1;
total = 0;
while i<354294:
    i+=1;
    i=str(i);
    isum=0;
    for num in i:
        isum+=int(num)**5;
    i=int(i);
    if isum == i:
        total+=i;
print(total);
