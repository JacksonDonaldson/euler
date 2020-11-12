largest = 0
for a in range(1,101):
    for b in range(1,101):
        n = a ** b
        n = str(n)
        total = 0
        for i in n:
            total += int(i)
        if total>largest:
            largest = total
