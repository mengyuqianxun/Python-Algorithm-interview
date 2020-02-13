class Maze:
    def __init__(self):
        self.n = 4

    def isFeasible(self,maze,x,y):
        return x>=0 and x<self.n and y>=0 and y<self.n \
            and maze[x][y] ==1
    
    def getPath(self,maze,x,y,path):
        if x == self.n - 1 and y == self.n - 1:
            path[x][y] = 1
            return True
        if self.isFeasible(maze,x,y):
            path[x][y] = 1
            if self.getPath(maze,x+1,y,path):
                return True
            if self.getPath(maze,x,y+1,path):
                return True
            path[x][y] = 0
            return False
        return False
    
    def printPath(self,path):
        i = 0
        while i <self.n:
            j = 0
            while j < self.n:
                print(path[i][j],end = ' ')
                j += 1
            print('\n')
            i += 1

if __name__ == "__main__":
    test = Maze()
    maze = [[1,0,0,0],[1,1,0,1],[0,1,0,0],[1,1,1,1]]
    path = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    if not test.getPath(maze,0,0,path):
        print(u'不存在可到的路径')
    else:
        test.printPath(path)