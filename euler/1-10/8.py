num = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450";
i = 0;
array = [];
while i<len(num):
    array.append(num[i]);
    i+=1;
#the part from here
def remove(start, finish):
    global array;
    print("removing from");
    print(start);
    print(finish);
    count = start;
    while count<finish+1:
        array.pop(start);
        count+=1;
    
zeroes = True;
toRemove = [];
while zeroes:
    i=0;
    while 1==1:
        if array[i] == "0":
            array[i] = 1;
            start = i-12;
            if start<0:
                start =0;
            count = 0;
            while count<12:
                if array[i+count] == "0":
                    array[i] = 1;
                    i = i+count;
                    count = 1;
                else:
                    count+=1;
                if i+count == len(array):
                    count-=1;
                    break
            finish = i+count;
            while start<finish+1:
                toRemove.append(start);
                start+=1;
            #remove(start, finish);
            break
        i+=1;
        if i == len(array):
            zeroes = False;
            break
i=0;
toPop = array;
array = [];
while i<len(toPop):
    if i in toRemove:
        i+=1;
        continue
    else:
        array.append(toPop[i]);
        i+=1;
print(array);
#to here breaks it, and is useless
biggest = 0;
i=0;
while i<len(array)-11:
    total = int(array[i]);
    i2=i;
    while i2<i+12:
        total = total * int(array[i2]);
        i2+=1;
    print("total from:" + str(i) + "to" + str(i2));
    print(total);
    if total>biggest:
        biggest = total;
    i+=1;
print(biggest);









        
    
    
