times = [1,1,3,2,5,3]
add = [1,0,-1,-1,-3,-2]
def generateNum(base, n):
    toReturn = n * (n * times[base-3] +add [base-3])
    if base % 2 == 1:
        toReturn /=2
    return int(toReturn)

#using generateNum, generates a list possibles of the possibilities for polynomial numbers that are 4 digits
possibles = []
for base in range(3,9):
    thisPossible = []
    i = 0
    while len(str(generateNum(base,i))) != 4:
        i+=1
    while len(str(generateNum(base,i))) == 4:
        thisPossible.append(str(generateNum(base,i)))
        i+=1
    possibles.append(thisPossible.copy())


#given some num, tests each thing in the list of lists nextList to see if it follows the circular rule. If none found, returns false. If 
def findPossibleNexts(num, nextLists,finalLoopCheck):
    tester = num[2:]
    isLastLoop = len(nextLists) == 1
        
    for nextList in range(len(nextLists)):
        for nextValue in nextLists[nextList]:

                #this is a possible for the next layer- it has the same starting 2 nums as the end of num
                #add an aditional test for possibleNexts with this num, and not including the list we took it from
            if nextValue[:2] == tester:
                #print("possible found")
                if isLastLoop:
                    #If we're on the last loop, then check to see if it'll circle around. If it will, return it and win
                    if nextValue[2:] == finalLoopCheck:
                        print("returning NextValue")
                        print(nextValue)
                        return nextValue

                else:
                    #we aren't on the final loop, so we have to go deeper. 
                    nextChecker = nextLists.copy()
                    nextChecker = nextChecker[0:nextList] + nextChecker[nextList + 1:]
                    
                    if findPossibleNexts(nextValue, nextChecker, finalLoopCheck):
                        print("value found!")
                        return [nextValue, findPossibleNexts(nextValue, nextChecker, finalLoopCheck)]

triangle = possibles.pop(0)
for tri in triangle:
    if findPossibleNexts(tri, possibles, tri[:2]):
        print("eyyy")
        print(tri)
        print(findPossibleNexts(tri, possibles, tri[:2]))
    print(tri)
                    
                    
                    

                
