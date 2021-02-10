import math
import itertools
i = 0;


#find all possible n digit ends to the permutations of the number
def findPerms(n, num):
    j = list(itertools.permutations(num,n))
    for number in range(0,len(j)):
        num = ""
        for i in range(n):
            num+= j[number][i]
        j[number] = num
    return j
#setup for checkCube
maps = {}

for i in range(0,10000):
    try:
        #print("attempting to set " + str(i) + "'s cube end in the database.")
        #print("checking to see if some other number already ends in this")
        maps[str(i * i * i)[-6:]] = i
        #print("no error, so some other number has already filled the spot that this would occupy. That number is " + str(maps[str(i * i * i)[-3:]]) +", and it is equal to " + str(i))
        #print("this would be bad")
        
    except:
        #print("No number was found. Setting up this number")
        maps[str(i * i * i)[-6:]] = i
        
##returns the number that a cube ending in num would have to be(maps ends to cubes)
def checkCube(num):
    try:
        return str(int(math.pow(maps[num],3)))
    except:
        return "0"

#given 2 numbers, checks to see if one is a permutation of the other
def checkPerm(n1, n2):
    totals = [0,0,0,0,0,0,0,0,0,0]
    for n in n1:
        totals[int(n)] +=1
    for n in n2:
        totals[int(n)] -=1
    for t in totals:
        if t!=0:
            return False
    return True



soughtCubes = 5

for i in range(100,10000):
    num = i * i * i;
    if(i % 10 == 0):
        print(i)
    perms = findPerms(6, str(num));
    #print("permed")
    perms = list(set(perms))
    #print("setted")
    
    #print(perms)
    cubes = 0
    for p in perms:
        foo = checkCube(p)
        if checkPerm(foo,str(num)):
            #print("cube found")
            cubes+=1
    
    #print("cubechecked")
    if cubes == soughtCubes:
        print(perms)
        print(num)
        print(i)
        break

#checked to 5027
