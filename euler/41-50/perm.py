def perm(start, num):
    if num == start:
        return str(start)
    done = perm(start, num-1);
    todo=[];
    for pos in done:
        for i in range(0, len(pos)+1):
            thing = pos[0:i]+ str(num) + pos[i:];
            todo.append(thing);
    return todo
