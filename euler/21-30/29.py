nums=[];
for a in range(2,101):
    for b in range(2,101):
        nums.append(a**b);
print('done');
nums.sort();
print('sorted');
norep=[];
for num in nums:
    if num not in norep:
        norep.append(num);
print(len(norep));
