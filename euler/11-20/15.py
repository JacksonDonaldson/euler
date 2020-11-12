known=[];
result=[];
def rc(x,y):
    if x==0:
        return 1
    elif y==0:
        return 1
    if x ==15 and y==15:
        return 155117520
    if x==16 and y==16:
        return 601080390
    if x==17 and y==17:
        return 2333606220
    if x==18 and y==18:
        return 9075135300
    if x==20 and y==20:
        return 137846528820
    else:
        total = 0;
        while y>=0:
            total = total + rc(x-1,y);
            y-=1;
        return total
rc(2,2);
        
            
