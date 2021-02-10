key = ["0","00","000","01","1","10","100","1000","02"]
hundredKey = ["C","D","M"]
tenKey = ["X","L","C"]
oneKey = ["I","V","X"]
def generateRoman(n):
    roman = ""
    while n>=1000:
        n-=1000
        roman += "M"
    if len(str(n)) == 3:
        hundreds = int(n/100)
        if hundreds != 0:
            toAppend = key[hundreds-1]
            for append in toAppend:
                roman += hundredKey[int(append)]
        n = int(str(n)[1:])
    if len(str(n)) == 2:
        tens = int(n/10)
        if tens !=0:
            toAppend = key[tens-1]
            for append in toAppend:
                roman += tenKey[int(append)]
        n = int(str(n)[1:])
    if len(str(n)) == 1:
        ones = int(n/1)
        if ones !=0:
            toAppend = key[ones-1]
            for append in toAppend:
                roman += oneKey[int(append)]
    return roman

def interpretRoman(roman):
    rToA = {"M":1000, "C":100, "D":500, "L":50, "X":10, "V":5, "I":1}
    lastNum = rToA[roman[0]]
    total = 0
    for romanNumeral in roman:
        if rToA[romanNumeral] > lastNum:
            total -= 2 * lastNum
        total += rToA[romanNumeral]
        lastNum = rToA[romanNumeral]
    return total


lines = open("89text.txt").readlines()
print(lines[0])
for l in range(len(lines)):
    lines[l] = lines[l][:-1]
lines[-1] += "I"

totalDif = 0
for line in lines:
    if interpretRoman(generateRoman(interpretRoman(line))) != interpretRoman(line):
        print("error!")
    dif = len(line) - len(generateRoman(interpretRoman(line)))
    if dif < 0:
        print("Less than 0!")
    totalDif += dif
print(totalDif)
#not 740, 1064


