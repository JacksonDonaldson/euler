a = 1;
while a<1000:
    b = 1;
    while b<1000:
        c = b+1;
        while c<1000:
            if (a**2 + b**2) == c**2:
                if a+b+c == 1000:
                    print(a);
                    print(b);
                    print(c);
            c+=1;
        b+=1;
    print(a);
    a+=1;
