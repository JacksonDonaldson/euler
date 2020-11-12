def ct(base,current):
    current[-1]+=1;
    while base in current:
        i = -1;
        while i>=-1*len(current):
            if current[i] == base:
                if i == -1 *len(current):
                    current.insert(0,0);
                    current[i] = 0;
                    
                else:
                    current[i-1]+=1;
                    current[i] = 0;
            i-=1;
    return current
