tri = [];
while True:
    this = input();
    if this=='done':
        break
    stor = [];
    i=0;
    while i<len(this):
        stor.append(int(this[i:i+2]))
        i+=3;
    
    tri.append(stor);
    if len(stor) ==100:
        break

i=2;
while i<len(tri)+1:
    j=0;
    while j<len(tri[-i]):
        tri[-i][j]+=max(tri[-i+1][j], tri[-i+1][j+1]);
        j+=1;
    i+=1;

    
