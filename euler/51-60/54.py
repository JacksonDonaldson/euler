
f = open("poker.txt").read()
f = f.replace(" ", "")
f = f.replace("\n", "")
threes = 0;
hands = []
for i in range(0,1000):
    hand = []
    for j in range(0,5):
        hand.append(f[i*20 + j*2: i*20+j*2 + 2])
    hands.append(hand)
    hand = []
    for j in range(0,5):
        hand.append(f[10 +i*20 + j*2: 10 + i*20+j*2 + 2])
    hands[-1] = [hands[-1], hand]


def score(hand):
    #print(hand)
    global threes
    for i in range(0,len(hand)):
        if hand[i][0] == "T":
            #print("fail")
            #print(hand[i])
            hand[i] = [10,hand[i][1]]
            #print(hand[i])
        elif hand[i][0] == "J":
            hand[i] = [11, hand[i][1]]
        elif hand[i][0] == "Q":
            hand[i] = [12, hand[i][1]]
        elif hand[i][0] == "K":
            hand[i] = [13, hand[i][1]]
        elif hand[i][0] == "A":
            hand[i] = [14, hand[i][1]]
        else:
            hand[i] = [int(hand[i][0]), hand[i][1]]
    #print(hand)
    hand.sort()
    suit = hand[0][1]
    same = True
    for card in hand:
        if card[1] != suit:
            same = False
            
            break
    consec = True
    for i in range(0,4):
        if int(hand[int(i)][0]) + 1 != hand[i+1][0]:
            consec = False
            break
##        except:
##            print("AHHH")
##            print(hand)
    if(consec):
        print("straight!")
    if(same and consec):
        print("royal flush!")
        return [8,hand[-1][0]]
    for i in range(0,2):
        if hand[i][0] == hand[i+1][0] and hand[i+1][0] == hand[i+2][0] and hand[i+2][0] == hand[i+3][0]:
            print("4 of a kind!")
            return[7, hand[i][0]]
    for i in range(0,3):
        if hand[i][0] == hand[i+1][0] and hand[i+1][0] == hand[i+2][0]:
            if i == 0:
                if hand[3][0] == hand[4][0]:
                    print("full house!")
                    return[6, max([hand[i][0], hand[4][0]])]
            elif i == 2:
                if hand[0][0] == hand[1][0]:
                    print("full house!")
                    return[6, max([hand[i][0], hand[0][0]])]
    if(same):
        print("Flush!")
        return [5, 0]
    if(consec):
        print("Straight!")
        return [4, 0]
    for i in range(0,3):
        if hand[i][0] == hand[i+1][0] and hand[i+1][0] == hand[i+2][0]:
            print("3 of a kind!")
            threes +=1
            return [3, hand[i][0]]
    
    if hand[0][0] == hand[1][0] and hand[2][0] == hand[3][0]:
        return [2, max([hand[0][0], hand[2][0]])]
    elif hand[2][0] == hand[1][0] and hand[4][0] == hand[3][0]:
        return [2, max([hand[1][0], hand[3][0]])]
    elif hand[0][0] == hand[1][0] and hand[4][0] == hand[3][0]:
        return [2, max([hand[1][0], hand[3][0]])]

    for i in range(0,4):
        if hand[i] == hand[i+1]:
            return[1, hand[i][0]]

    return [0,0]
def maxValue(hand):
    hand.sort()
    return hand[-1][0]
p1wins = 0
for match in hands:
    if score(match[0])[0]>score(match[1])[0]:
        #print(match[0])
        #print(match[1])
        p1wins+=1
    elif score(match[0])[0] == score(match[1])[0]:
        if score(match[0])[1] > score(match[1])[1]:
            p1wins+=1
        else:
            if maxValue(match[0])>maxValue(match[1]):
                p1wins+=1
            elif maxValue(match[0]) == maxValue(match[1]):
                if maxValue(match[0][0:4])>maxValue(match[1][0:4]):
                    p1wins+=1
                elif maxValue(match[0][0:4]) == maxValue(match[1][0:4]):
                    if maxValue(match[0][0:3])>maxValue(match[1][0:3]):
                        p1wins+=1;
                    elif maxValue(match[0][0:3]) == maxValue(match[1][0:3]):
                        print("AAAH")
                        
        
print(p1wins)
