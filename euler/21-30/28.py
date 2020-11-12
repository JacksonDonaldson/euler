diagonals=[1];
i = 2;
while i!=1002:
    diagonals.append(diagonals[-1]+i);
    diagonals.append(diagonals[-1]+i);
    diagonals.append(diagonals[-1]+i);
    diagonals.append(diagonals[-1]+i);
    i+=2;
print(sum(diagonals));
#I didn't really expect this to work, but I guess it was this easy
