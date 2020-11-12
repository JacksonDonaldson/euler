import time;
start = time.time();
i = 0;
done = False;
def check(num, div):
    if num % div == 0:
        return 1
    else:
        return 0
while not done:
    i+=20;
    div = 20;
    while True:
        if check(i, div) == 1:
            if div==10:
                print(i);
                print(time.time()-start);
                done = True
                break
        else:
            break
        div-=1;
            
        
        


    
