def createMaze():
    maze = [] 
    maze.append([" "," "," "]) 
    maze.append(["#","#"," "]) 
    maze.append(["x"," "," "])             
    return maze;
def getValidMoves(maze,currentPos):
    validMoves = []
    row = currentPos[0]
    col = currentPos[1]
    
    if( row < len(maze[0])-1 and maze[row +1][col] != "#"  ):
        validMoves.append("D")
    if( row > 0 and maze[row -1][col] != "#"   ):
        validMoves.append("U")
    
    if( col < len(maze[0])-1 and maze[row][col + 1] != "#" ):
       validMoves.append("R")
    if(col > 0 and  maze[row][col-1] != "#"  ):
         
        validMoves.append("L")
    
    return validMoves
print(len(createMaze()[0]))
print(getValidMoves(createMaze(),[2,2]))
