array = [1,1];
while array[-1] < 4000000:
    array.append(array[-1] + array[-2]);
del(array[-1]);
i=0;
total = 0;
while i < len(array):
    if array[i]%2==0:
        total += array[i];
    i+=1;
print(total);
    
