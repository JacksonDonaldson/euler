import math

def prime(n):
    for i in range(2,math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def primeList(n):
    l = []
    i=2
    while len(l)<n:
        if prime(i):
            l.append(i)
        i+=1
    return l

def minSequences(n):
    pList = primeList(4 * n)
    sequences = [[0,1,2,3]]
    while len(sequences) < n:
        options = []
        for index in sequences[-1]:
            if index+1 not in sequences[-1]:
                options.append([index, index+1])

        #now we have everything that could reasonably increase
        #check to see if there are any decreases that could be made to balance out
        #if the max decrease already appears, go up a level (and repeat unti we reach og)
        #for each option:
            #while canMakeADecrease:
                #make all available decreases, seperately and together
                #store all possible results
                
        for option in options:
            lowerability = []
            c = sequences[-1].copy()
            c[c.index(option[0])] = option[1]
            for i in c:
                #at each index, check to see if it can be lowered. It can be lowered at max to whatever the next lowest number + 1 is.
                j = 1
                while i - j not in c and i - j >= 0:
                    j += 1
                j-=1
                #i can be lowered at most j
                lowerability.append(j)
            option.append(lowerability)

        #now, we have each reasonable option
            #multi-number lowerability... ffs

                
        
        minValue = 9999999999999999

        #print(options)
        for option in options:
            value = pList[option[1]] - pList[option[0]]
            if value < minValue:
                minValue = value
                minOption = option
        toA = sequences[-1].copy()
        toA[toA.index(minOption[0])] = minOption[1]
        sequences.append(toA)
    return sequences

sequences = minSequences(10000)
p = primeList(3000)
for sequence in sequences:
    for i in range(0,len(sequence)-1):
        good = True
        for j in range(i+1, len(sequence)):
            if not prime(int(str(p[i]) + str(p[j]))):
                good = False
                break
        if not good:
            break
    if good:
        print(sequence)
