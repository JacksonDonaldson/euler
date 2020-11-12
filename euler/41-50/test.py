for x in range(1,10000):
    for y in range(1,10000):
        if x**2 + y**2 > (x+y)**2:
            print('bad')
