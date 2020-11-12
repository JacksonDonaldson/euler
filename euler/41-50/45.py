tri =[]
for i in range(1,1000000):
    tri.append((i*i+i)/2)
pent =[]
for i in range(1,200000):
    pent.append((3*i*i-i)/2)
hexa=[]
for i in range(1,100000):
    hexa.append(i*2*i-i)
for trin in tri:
    if trin in hexa:
        if trin in pent:
            print(trin)
            
#works eventually. better way: check if hexagonal/pentagonal: divide by 2n-1 or whatever
