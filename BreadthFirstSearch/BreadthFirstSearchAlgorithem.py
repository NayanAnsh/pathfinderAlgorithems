import queue
import time
from maze.mazeExtractor import maze as mazeClass
#Tip : You can create easy maze code from mazeCodeCreator.py
mazeName= "maze102" #  file path for mazes E:\python programs\pathfinderAlgorithems\maze
def findEnd(maze):
    #Searches for Ending point(x)  in maze
    r =-1 #Row coordinate
    c = -1 # Column Coordinate
    for rowPos,row in enumerate(maze):
        for elementPos,element in enumerate(maze[rowPos]):
            if element == "x":
                r = rowPos
                c = elementPos
    
    return [r,c];

def findStart(maze):
    #Searches for staring point(0) in maze
    r =-1 #Row coordinate
    c = -1 # Column Coordinate
    for rowPos,row in enumerate(maze):
        for elementPos,element in enumerate(maze[rowPos]):
            if element == "0":
                r = rowPos
                c = elementPos
    
    return [r,c];
def getCurrentPos(maze,startPos,movesMade):
    row = startPos[0]
    col = startPos[1]
    for m in movesMade:
        if m == "L":
            col -=1
        elif m =="R":
            col += 1 
        elif m == "U":
            row -= 1
        elif m == "D":
            row += 1
        
    return [row,col]
    
def getValidMoves(maze,currentPos,lastpath):
    lastmove = ""
    if lastpath != "":
        #Do not move back to last square
        lastmove = lastpath[len(lastpath)-1]
    validMoves = []
    row = currentPos[0]
    col = currentPos[1]
    
    if( row < len(maze[0])-1 and maze[row +1][col] != "#" and lastmove != "U" ):
        validMoves.append("D")
    if( row > 0 and maze[row -1][col] != "#"  and lastmove != "D" ):
        validMoves.append("U")
    
    if( col < len(maze[0])-1 and maze[row][col + 1] != "#"  and lastmove != "L"):
       validMoves.append("R")
    if(col > 0 and  maze[row][col-1] != "#" and lastmove != "R" ):
         
        validMoves.append("L")
    
    return validMoves
def main(maze):
    startTime = time.time()
    print("Starting breadthFirst Search")
    # n is dimension of maze nxn
    pathExplored = [] # variable is also called in boardCheckerMain.py
    maze =  maze
    startPos =   findStart(maze)   
    endPos =  findEnd(maze)
    currentPos = startPos
    q = queue.Queue()
    add = ""
    q.put("")
    steps  = 0
    while endPos != currentPos:
        add = q.get()
        currentPos = getCurrentPos(maze, startPos, add)
        #print(add)
        if add != "":
            pathExplored.append(add)
        #print(currentPos)
        steps +=1;
        for j in getValidMoves(maze,currentPos,add):
            q.put(add +j)
        if steps > 50000:
            
            print("Failed:Too many steps unable to find it")
            break
        
    print("Shortest Path = "+add)
    print("Total steps - "+ str(steps))
    shortestPath = add
    print("Time taken to solve maze ," ,(time.time()-startTime))
    return shortestPath,pathExplored #shortestPath,All path explored return type list,list
m = mazeClass(mazeName)
maze = m.extractMaze()
#main(maze)