def perm(num):
    if num == 0:
        return '0'
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
print(perms[999999]);
