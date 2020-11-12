import prime
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
perms=perm(7);
biggest=0;
print('perms found');
for per in perms:
    if prime.p(int(per)):
        if int(per)>biggest:
            biggest = int(per);

print(biggest);
