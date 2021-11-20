def palFind(find, l):
    savFind = find
    for element in l:
        find = savFind
        if(len(element) != len(find)):
            continue
        for character in element:
            
            try:
                find = find[0:find.index(character)] + find[find.index(character)+1:]
            except:
                if(find ==""):
                    break
                pass
        #print(find)
        else:
            if find == "":
                return True    
    return False

def findSquarePalindromes(length):
    i = 4
    squares = []
    while len(str(i**2)) < length:
        squares.append(str(i**2))
        i+=1
    pals = []
    for e in squares:
        copy = squares.copy()
        copy.remove(e)
        if palFind(e,copy):
            pals.append(e)
    return pals
#not 355572, because that includes those with more than 1 possible way to make them.
