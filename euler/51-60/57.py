import math
def collapseFraction(num, fract):
    #takes a number and a fraction, and returns a fraction representing them added together
    fract[0] += num * fract[1]
    return fract.copy()

def findApproximation(length):
    #returns an array of a numerator and demononator that represents an approximation of sqrt 2 to depth length
    workingDenom = collapseFraction(2,[1,2])

    for i in range(length-3,-1,-1):

        #represents the "1/" this fraction
        workingDenom.reverse()
    
        workingDenom = collapseFraction(2,workingDenom)
    workingDenom.reverse()
    workingDenom[0] += workingDenom[1]
    
    return workingDenom

total = 0
for i in range(7, 1001):
    approx = findApproximation(i)
    if int(math.log10(approx[0])) > int(math.log10(approx[1])):
        print(approx)
        total +=1

print(total)
