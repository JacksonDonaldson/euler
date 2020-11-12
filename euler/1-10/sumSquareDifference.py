i = 1;
total = 0;
while i<101:
    total+=i;
    i+=1;
total = total*total;
i = 1;
total2 = 0;
while i<101:
    total2 += i*i;
    i+=1;
    print(total2);
print(total-total2);
