i = 1;
i2 = 1;
biggest = 0;
total = 0;
temp = 0;
good = 1;
while i < 1000:
    while i2 < 1000:
        total = str(i*i2);
        
        if len(str(total))%2 == 0:
            temp = len(str(total))/2;
        else:
            temp = len(str(total))/2 - 0.5;
        count = 0;
        good = 1;
        while count < temp:
            if total[count] != total[-1*(count+1)]:
                good =0;
            count +=1;
        if good:
            if int(total)>biggest:
                biggest = int(total);
        i2+=1;
    i+=1;
    i2=1;
print(biggest);
