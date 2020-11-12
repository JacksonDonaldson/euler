i=0;
biggest=0;
biggestNum=0;
import math
import basecount
import time
current=time.time();

def prime(n):
    if n<2:
        return False
    if n==2 or n==3 or n==5 or n==7:
        return True
    if n<11:
        return False
    for i in range(2,math.ceil(math.sqrt(n))+1):
        if n%i ==0:
            return False
    return True
done=[]
def check(n):
    global current
    global done
    global biggest
    global biggestNum
    if n not in done:
        done.append(n);
        total=0;
        #something that replaces n with all numbers
        ap='';
        value=[-1];
        for somethingrandom in range(1,n.count('n')):
##            print(value);
            value.insert(0,0);
##        print('value done');
##        print(n);
##        print(value);
##        print(n.count('n'));
        for a in range(0,10**n.count('n')):
            total=0;
            value = basecount.ct(10,value);
            for b in range(0,10):
                
                index=0;
                ap='';
                for num in n:
                    if num == '*':
                        ap+=str(b);
                    else:
                        ap+=str(value[index]);
                        
                        index+=1;
                try:
                    if len(ap) == len(str(int(ap))):
                        if prime(int(ap)):
                            total+=1;
                except:
                    print('fail at int(ap)');
                    print(ap);
            if total==8:
                print(total);
                
                biggest=total;
                biggestNum = [n, a,];
                print(biggestNum);
                print(time.time()-current);
                quit();
def replace(array):
    i=0;
    dummy=list(array);
    for num in dummy:
        dummy=list(array);
        if num == '*':
            i+=1;
            continue
        dummy[i] = '*';
        check(dummy);
        replace(tuple(dummy));
        #print('done');
        i+=1;
array=[];
while biggest !=7:
    array.append('n');
    #print('replacing');
    #print(i);
    replace(tuple(array));
print(biggestNum);
