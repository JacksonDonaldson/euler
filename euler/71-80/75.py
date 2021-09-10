import math
#find minimal form and multiply out is the play

totals = set()

for i in range(2,1500000):
    big = i ** 2
    for j in range(1,i):
        if(math.sqrt(big-j**2).is_integer()):
            totals.add(i + j + math.sqrt(big-j**2))
    if(i%1000 == 0):
        print(i)
print(len(totals))
#not 579
        
