import perm
perms = perm.perm(0,9)
total=0
for n in perms:
    
    if int(n[1:4])%2==0 and int(n[2:5])%3==0 and int(n[3:6])% 5 ==0 and int(n[4:7])% 7 == 0 and int(n[5:8]) % 11 ==0 and int(n[6:9]) % 13 == 0 and int(n[7:10]) % 17 ==0:
        total+= int(n)
print(total);
        
    
