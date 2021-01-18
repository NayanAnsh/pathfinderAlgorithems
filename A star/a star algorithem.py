normalMoveCost = 1

class Node:
    def __init__(self,parent,pos,g,h):
        self.parent =  parent
        self.position = pos
        self.g = g #Total cost from start ot current node
        self.h = h #Estimated cost from current node to end node
        self.f = self.g + self.h # g + h value 
   
    def __eq__(self, other): 
        if not isinstance(other, Node):
            
        # don't attempt to compare against unrelated types
            return NotImplemented

def createMaze(n):
    
    # n is dimension of maze nxn
    maze = [] 
    if n == 3:
        
        maze.append([" "," "," "]) 
        maze.append(["#","#","0"]) 
        maze.append(["x"," "," "])             
        
    elif n == 5:
        
        maze.append(["#"," ","#","0","#"]) 
        maze.append([" ","#","#"," "," "]) 
        maze.append([" "," "," ","#"," "]) 
        maze.append([" ","#"," "," "," "]) 
        maze.append(["x","#"," ","#"," "]) 
        
    elif n == 10:
         
        maze.append([" ","#"," ","#"," "," "," "," ","#","#"]) 
        maze.append([" "," "," "," "," ","#","x"," "," "," "]) 
        maze.append(["#","#","#","#","#"," "," ","#","#"," "]) 
        maze.append(["#"," "," "," "," "," "," "," "," "," "]) 
        maze.append(["#"," ","#"," ","#"," ","#","#"," "," "]) 
        maze.append(["#"," "," ","#"," "," ","#"," "," "," "]) 
        maze.append(["#"," "," "," "," "," "," "," "," ","#"]) 
        maze.append(["#"," ","#","#","#"," ","#","#","#","#"]) 
        maze.append(["#"," ","#"," ","#"," ","#"," ","#"," "]) 
        maze.append(["#","0","#","#","#","#","#","#","#","#"])
    elif n == 11:
        maze.append(["#","0"," "," "," "," "," "," ","#"," ","#"])
        maze.append(["#","#"," ","#","#"," ","#"," ","#"," ","#"])
        maze.append(["#"," "," "," ","#"," ","#"," ","#"," ","#"])
        maze.append(["#"," ","#","#","#"," "," "," ","#"," ","#"])
        maze.append(["#"," ","#"," "," "," ","#"," "," "," ","#"])
        maze.append(["#"," "," "," ","#"," ","#"," ","#"," ","#"])
        maze.append(["#"," ","#"," "," "," "," "," ","#"," ","#"])
        maze.append(["#"," ","#","#","#","#","#","#","#"," ","#"])
        maze.append(["#"," "," "," "," "," "," "," "," ","x","#"])
        maze.append(["#","#","#","#","#","#","#","#","#","#","#"])
        maze.append(["#","#","#","#","#","#","#","#","#","#","#"])
        
    elif n == 100:
        #DO NOT USE THIS  CONDITION 
        file =  open("E:\python programs\pathfinderAlgorithems\BreadthFirstSearch\maze001.txt","r")
        maze = []
        for line in file:
            maze.append(list(line.replace("\n", "")))
    else:
        print("Only 3 5 10 11 as argument of main func is valid")
    return maze
def getchildPos(maze,parentPos,move):
    row = parentPos[0]
    col = parentPos[1]
    
    if move == "L":    
        col -=1
    elif move =="R":
        col += 1 
    elif move == "U":
        row -= 1
    elif move == "D":
        row += 1
        
    return [row,col]
    
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
def heuristic(current_Node,end_node):
    D =1
    dx = abs(current_Node.position[0] - end_node.position[0] )
    dy = abs(current_Node.position[1] - end_node.position[1])
    return D * (dx + dy)
def getValidMoves(maze,currentPos,visited):
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
    for node in visited:
        #Not checing boxes already visited again
        for m in validMoves:
            pos = getchildPos(maze, currentPos, m)
            if pos == node.position:
                validMoves.remove(m)
                
    return validMoves

    
maze =  createMaze(11)
startPos =  findStart(maze)
endPos = findEnd(maze)

start_node = Node(None,startPos,0,0)
end_node = Node(None,endPos,0,0)

current_Node  =  start_node
visited = []
not_visited = []
print("starting loop")
j = 0 
while(current_Node.position != endPos ):
    visited.append(current_Node)
    print(current_Node.position)
    moves =  getValidMoves(maze,current_Node.position,visited)
    print(moves)
    for move  in moves:
        g = current_Node.g + normalMoveCost
        h = heuristic(current_Node,end_node)
        childpos = getchildPos(maze, current_Node.position, move)
        print(childpos)
        new_node=Node(current_Node,childpos,g,h)
        
        not_visited.append(new_node)
    
    current_Node = not_visited[0]
    for i,node in enumerate(not_visited):
        
        current_Node_index = None
        #print(node.position ," vs ",current_Node.position)
        #print(node.f , " vs ", current_Node.f)
        #print(node.h , " vs ",current_Node.f)
        if node.f < current_Node.f:
            current_Node = node
            current_Node_index = i
    not_visited.remove(current_Node)
    j +=1
    print()
print("Path founded")
print(j)
node = current_Node
finalepathPos = []
finalepathPos.append(node.position)
while(node.parent != None):
    
    finalepathPos.append(node.parent.position)
    node = node.parent
finalepathPos.reverse()

d = finalepathPos[0]
finalepathPos.remove(d)
print(d)
finalePath = []
print(finalepathPos)
for pos in finalepathPos:
    px =  pos[0]-d[0]
    py =  pos[1]-d[1]
    movee = ""
    if px == 1:
        movee = "D"
    if px == -1:
        movee = "U"
    if py == -1:
        movee = "L"
    if py == 1:
        movee = "R"
    finalePath.append(movee)
    d = pos
print("".join(finalePath))












