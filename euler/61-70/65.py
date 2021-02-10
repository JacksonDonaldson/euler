def geneList(length):
    l = []
    for i in range(1,int(length/3)+1):
        l.append(1)
        l.append(i*2)
        l.append(1)
    return l

def collapseFraction(num, fract):
    #takes a number and a fraction, and returns a fraction representing them added together
    fract[0] += num * fract[1]
    return fract.copy()

def findApproximation(length):
    divisors = geneList(length)

    workingDenom = collapseFraction(divisors[length-2],[1,divisors[length-1]])

    for i in range(length-3,-1,-1):

        #represents the "1/" this fraction
        workingDenom.reverse()
    
        workingDenom = collapseFraction(divisors[i],workingDenom)
    workingDenom.reverse()
    
    return workingDenom

total = 0
f= findApproximation(99)
f[0] += 2 * f[1]
for digit in str(f[0]):
	total += int(digit)

print(total)
