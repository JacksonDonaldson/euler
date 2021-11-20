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
                        return False
                    if not self.removeGridSames(x,y):
                        return False
        return True

    def replaceSingle(self):
        for x in range(9):
            for y in range(9):
                if type(self.grid[x][y]) is Blank and self.grid[x][y].single:
                    self.grid[x][y] = self.grid[x][y].getNum()

    def cycle(self):
        if not self.removeAllCurrentImpossible():
            return False
        self.replaceSingle()
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
        return grid.grid
    i=0
    
    while i < 81:
        if cycle < 4:
            print(grid.toString())
        while i < 80 and type(grid.grid[i//9][i%9]) is int:
            i+=1
            
        if i == 80:
            if type(grid.grid[8][8]) is int:
                break
        g2 = copy.deepcopy(grid)
        try:
            for j in range(len(grid.grid[i//9][i%9].potentialNums)):
            
                g2.grid[i//9][i%9] = grid.grid[i//9][i%9].potentialNums[0]
                r = guessAndCheck(g2, cycle + 1)
                if r:
                    return r
        except:
            print(i)
            quit()
        i+=1
    return False
  
    
g = readGrids()
g[-1][-1].append(6)
i = 0
count = 0
for f in g:
    i+=1
    print(i)
    g0 = Grid(f)
    
    g0.runCycles()
    if g0.full():
        count+=1
        print("success!")
    else:
        t = guessAndCheck(g0, 0)
        
        print("failed")
print(count)
