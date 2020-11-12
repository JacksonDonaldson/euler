def do(num):
    moves = 0;
    while num!=1:
        if num %2==0:
            num=num/2;
            moves+=1;
        else:
            num=num*3+1;
            moves+=1;
    return moves
