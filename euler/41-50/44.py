pent=[]
for i in range (1,2000000):
    pent.append(i/2*(3*i-1))
print('done');
possible=[];
for x in range(0,100000):
    for y in range(1,x):
        total = (3*x*x+3*y*y-x-y)/2
        if total in pent[max(x,y)-1:(x+y)+1]:
            possible.append([x,y])
            div = abs(((3*x*x)-(3*y*y)-x+y)/2)
            if div in pent[0:max(x,y)]:
                print('success!!!!!!!!')
                print(x)
                print(y)
                quit()
                

    if x%100 == 0:
        print(x)
