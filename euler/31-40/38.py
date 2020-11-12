def perm(num):
    if num == 1:
        return '1'
    done = perm(num-1);
    todo=[];
    for pos in done:
        for i in range(0, len(pos)+1):
            thing = pos[0:i]+ str(num) + pos[i:];
            todo.append(thing);
    print(num);
    return todo
perms = perm(9);
perms.sort();
print('found perms');
biggest=0;
for i in range(0,10000):
    concat=str(i);
    for j in range(2,9):
        concat+=str(j*i);
        if len(concat)>9:
            break
        if len(concat)==9:
            if concat in perms:
                if int(concat)>biggest:
                    biggest=int(concat);
print(biggest);
