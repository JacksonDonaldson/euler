import math
def getPeriod(quotient):
   
    numer = 1
    divis = -int(math.sqrt(quotient))
    values = [divis]
    #print(values)
    #print(numer, " ", divis)
    nextA = int(numer/(math.sqrt(quotient) + divis))
    #print(nextA)
    
    bot = quotient - divis * divis
    bot /= numer
    #print(bot)
    if(not bot.is_integer()):
        print("aaah")
    top = -divis - nextA * bot
    #print(top)
    numer = bot
    divis = top

    storDivis = divis
    storNumer = numer
    i=0    
    while True:
        i+=1
        #print(numer, " ", divis)
        nextA = int(numer/(math.sqrt(quotient) + divis))
        #print(nextA)
        
        bot = quotient - divis * divis
        bot /= numer
        #print(bot)
        if(not bot.is_integer()):
            print("aaah")
        top = -divis - nextA * bot
        #print(top)
        numer = bot
        divis = top

        values.append(nextA)
        if(divis == storDivis and numer == storNumer):
            break
    return i
total = 0        
for i in range(2,10001):
    if math.sqrt(i).is_integer():
        continue
    if getPeriod(i) % 2 == 1:
        total +=1
print(total)
