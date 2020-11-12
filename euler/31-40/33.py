good=[];
for a in range(10,100):
    for b in range(10,100):
        if a!=b and a%10!=0 and a/b<1:
            reduced=[];
            if str(a)[0] in str(b):
                reduced.append(int(str(a)[1]));
                if str(b)[0]==str(a)[0]:
                    #print('found');
                    reduced.append(int(str(b)[1]));
                else:
                    reduced.append(int(str(b)[0]));
            if str(a)[1] in str(b):
                reduced.append(int(str(a)[0]));
                if str(b)[0]==str(a)[1]:
                    reduced.append(int(str(b)[1]));
                else:
                    reduced.append(int(str(b)[0]));
            if reduced != []:
                #print(reduced);
                #print(a);
                #print(b);
                
                if reduced[1]!=0:
                        if reduced[0]/reduced[1]==a/b:
                            good.append([a,b]);
print(good[0][0]*good[1][0]*good[2][0]*good[3][0]);
print(good[0][1]*good[1][1]*good[2][1]*good[3][1]);
