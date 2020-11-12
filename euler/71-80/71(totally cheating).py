nums = set({})
smallest = 3/7
for a in range(10,1000001):
    i = 3*(a/7)
    if (3/7 - (int(i)/a)) < smallest:
        if((3/7 - (int(i)/a)) != 0):
            smallest = (3/7 - (int(i)/a))
            storI = i
            storA = a
