coins =[1,2,5,10,20,50,100];
coins.reverse();
known=[];
op=[];
for i in range(0,201):
    known.append("");
def waystomake(remaining):
    global coins
    ways=[];
    if known[remaining]!="":
        return known[remaining]
    for coin in coins:
        if remaining==coin:
            ways.append([coin]);
        if coin<remaining:
            tempways=waystomake(remaining-coin);
            for tempway in tempways:
                ways.append([coin]+tempway);
    for way in ways:
        way.sort();
    ways.sort();
    unrep=[];
    for way in ways:
        if way not in unrep:
            unrep.append(way);
    print(remaining);
    known[remaining]=unrep;
    return unrep
print(len(waystomake(200))+1);
##print('foundall');
##for option in op:
##    option.sort();
##unrep = [];
##for option in op:
##    if option not in unrep:
##        unrep.append(option);
##print(len(unrep));
