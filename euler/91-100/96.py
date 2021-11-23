import copy

class Blank():
    def __init__(self):
        self.potentialNums = list(range(1,10))
        self.single = False
        
    def removeNum(self, n):
        if type(n) is list:
            for i in n:
                if i in self.potentialNums:
                    self.potentialNums.remove(i)
        else:
            if n in self.potentialNums:
                self.potentialNums.remove(n)
        if(len(self.potentialNums) == 1):
            self.single = True
        if(len(self.potentialNums) == 0):
            return False
        return True

    def getNum(self):
        #print("num got!")
        if not self.single:
            raise Exception("not single!")
        if len(self.potentialNums) == 0:
            return False
        return self.potentialNums[0]
    
class Grid():
    
    def __init__(self, grid):
        self.grid = []
        for row in grid:
            r = []
            for value in row:
                if value == 0:
                    r.append(Blank())
                else:
                    r.append(value)
            self.grid.append(r.copy())


    def full(self):
        for r in self.grid:
            if Blank in [type(b) for b in r]:
                return False
        return True

    def removeCellSames(self, x,y):
        removeLocations = []
        xCell = x // 3
        yCell = y//3
        #print(f"x: {x}, y: {y}")
        for i in range(xCell*3,xCell*3+3):
            for j in range(yCell*3, yCell*3+3):
                #print([i,j])
                removeLocations.append([i,j])

        remove = []
        for r,c in removeLocations:
            if type(self.grid[r][c]) is not Blank:
                remove.append(self.grid[r][c])

        return self.grid[x][y].removeNum(remove)

    def removeGridSames(self, x,y):
        remove = []
        for i in range(9):
            if type(self.grid[i][y]) is not Blank:
                remove.append(self.grid[i][y])
            if type(self.grid[x][i]) is not Blank:
                remove.append(self.grid[x][i])
        return self.grid[x][y].removeNum(remove)

        
    def removeAllCurrentImpossible(self):
        for x in range(9):
            for y in range(9):
                if type(self.grid[x][y]) is Blank:
                    if not self.removeCellSames(x,y):
                        #print("remove cell fail")
                        return False
                    if not self.removeGridSames(x,y):
                        #print("remove cell fail2")
                        return False
        return True

    def replaceSingle(self):
        for x in range(9):
            for y in range(9):
                if type(self.grid[x][y]) is Blank and self.grid[x][y].single:
                    v = self.grid[x][y].getNum()
                    if not v:
                        #print(f"Failed at: x: {x}, y: {y}")
                        return False
                    #print(f"x: {x} y: {y}")
                    self.grid[x][y] = v
                    
                    self.removeAllCurrentImpossible()
        return True

    def getBox(self, i):
        #print(i)
        locations = []
        xCell = i // 3
        yCell = i % 3
        #print(f"x: {xCell}, y: {yCell}")
        for i in range(xCell*3,xCell*3+3):
            for j in range(yCell*3, yCell*3+3):
                #print([i,j])
                locations.append(self.grid[i][j])
        return locations
    
    def setOnlyPossibles(self):
        #check to see if the number can only be in one spot
        #print("start")
        for i in range(9):
            #print("calling only possible")
            row = self.grid[i]
            column = [self.grid[j][i] for j in range(9)]
            box = self.getBox(i)
            for j in range(1,10):
                #print(j)
                for element in [row,column, box]:
                    if j not in element:
                        #print(element)
                        spots = []
                        for value in element:
                            if type(value) is Blank:
                                if j in value.potentialNums:
                                    spots.append(value)
                        #print(spots)
                        if(len(spots) == 0):
                            return False
                        if(len(spots) == 1):
                            #print(spots[0].potentialNums)
                            spots[0].potentialNums = [j]
                            spots[0].single = True
                            
                            #print(j)
                            #print("found a only")

        return True



                    

    def cycle(self):
        if not self.removeAllCurrentImpossible():
            return False
        if not self.setOnlyPossibles():
            return False
        if not self.replaceSingle():
            return False


        return True

    def runCycles(self):
        prev = self.toString()
        if not self.cycle():
            return False
        while prev != self.toString():
            prev = self.toString()
            if not self.cycle():
                return False
        return True
        
    def toString(self):
        s = ""
        for i in range(9):
            s+=" ".join([str(j) if type(j) is not Blank else "0" for j in self.grid[i]])
            s+= "\n"
        return s
                
def readGrids():
    boards = []
    with open("96.txt") as file:
        for i in range(50):
            file.readline()
            board = []
            for i in range(9):
                board.append([int(i) for i in list(file.readline())[:-1]])
            boards.append(board.copy())
    return boards

def guessAndCheck(grid, cycle):
    if not grid.runCycles():
        return False
    if grid.full():
        return grid
    i=0
    
    while i < 81:
        if cycle == 0:
            print(grid.toString())
        while i < 80 and type(grid.grid[i//9][i%9]) is int:
            i+=1
            
        if i == 80:
            if type(grid.grid[8][8]) is int:
                break
        g2 = copy.deepcopy(grid)

        blank = g2.grid[i//9][i%9]
        nums = blank.potentialNums
        for j in range(len(nums)):
            #print(f"setting ({i//9}, {i%9}) to {nums[j]}")
            g2.grid[i//9][i%9] = nums[j]
            r = guessAndCheck(copy.deepcopy(g2), cycle + 1)
            if r:
                return r
            g2.grid[i//9][i%9] = blank
        i+=1
    return False
  
    
g = readGrids()
g[-1][-1].append(6)
i = 0
count = 0
total = 0
for f in g:
    i+=1
    print(i)
    g0 = Grid(f)
    
    g0.runCycles()
    if g0.full():
        count+=1
        print("success!")
        print(g0.toString())
        total += g0.grid[0][0] * 100 + g0.grid[0][1] * 10 + g0.grid[0][2]
    else:
        t = guessAndCheck(g0, 0)
        print(t.toString())
        print("failed")
        total += t.grid[0][0] * 100 + t.grid[0][1] * 10 + t.grid[0][2]
print(count)
print(total)
#not 19074
