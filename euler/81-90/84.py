landCount = [0] * 40
board = {}
ccSquares = [2,17,33]
chSquares = [7,22,36]
g2jSquare = 30

cc = [""] * 14
cc.extend([0,10])
ccCurrent = 0
ch = [0,10,11,24,39,5,"nR","nR","nU","-3","","","","","",""]
chCurrent = 0


import random
random.shuffle(ch)
random.shuffle(cc)


def roll():
    return random.randint(1,4)


currentSquare = 0
i=0
doublesCount = 0

while True:
    r1 = roll()
    r2 = roll()
    if r1 == r2:
        doublesCount +=1
        if(doublesCount == 3):
            currentSquare = 10
            doublesCount = 0
    else:
        doublesCount = 0
        currentSquare += r1+r2
        currentSquare %= 40

    
    if currentSquare in ccSquares:
        do = cc[ccCurrent]
        ccCurrent = (ccCurrent + 1) % 16
        if do == 0 or do == 10:
            currentSquare = do
            
        
    elif currentSquare in chSquares:
        do = ch[chCurrent]
        chCurrent = (chCurrent+1) % 16
        if do == "nR":
            if currentSquare == 2:
                currentSquare = 5
            if currentSquare == 17:
                currentSquare = 25
            if currentSquare == 33:
                currentSquare = 35
        elif do == "nU":
            if currentSquare == 2:
                currentSquare = 12
            if currentSquare == 17:
                currentSquare = 28
            if currentSquare == 33:
                currentSquare = 12
        elif do == "-3":
            currentSquare = (currentSquare - 3) % 40
        elif do != "":
            currentSquare = do

    elif currentSquare == g2jSquare:
        currentSquare = 10
        doublesCount = 0
    landCount[currentSquare] += 1
    i+=1
    
    if i % 2000000 == 0:
        temp = landCount.copy()
        for j in range(0,6):
            print(max(temp)/i * 100, "% at square ",landCount.index(max(temp)))
            temp.pop(temp.index(max(temp)))
        print()
        
