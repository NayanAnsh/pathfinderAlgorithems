
import pygame
import sys
import time
import math
import random
from BreadthFirstSearch.BreadthFirstSearchAlgorithem import  main as BFSMain
from Astar.a_star_algorithem import main as AStarMain
from maze.random_maze import random_maze
from maze.mazeExtractor import maze as mazeClass
#Variable for user to control
n = 20# n is dimension of maze nxn # Only 3 5 10 as argument of main func is valid
drawMazeOption = 2 # if 1 then darw a empty maze ..if 2 then extract maze if 3 then genrate a random maze
########if drawMazeOption = 2 then bellow variables will  be used###########
mazeName = "tyu"
########if drawMazeOption = 3 the bellow variables will  be used for random maze genrator###########
w = 100
h = 100
c = 0.9
d = 0.9
#Do not forget to set start and end 
####################################################################################################
minColor = 80 # minimum color value of rgb  allowed 
colorDecreaseValue = 100 # amount of color valueto decrease from r g b when program steps on same square
relativeColorChange =  True # if true then squares will chnage its color relative to its previous color
waitTime = 1 # wait time before start solving the maze
screenSize = width,height = 1000,1000 # dimension of window
searchChoice = 1 # 0  = breathFirst seatch 1 = A star Search



#print(screenSize)

#Colors Constant
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE =  (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)

#Global variables

def createEmptyMaze(n):
    maze =[]
    
    for i in range(0,n):
        m = []
        for j in range(0,n):
            m.append(" ")
        maze.append(m)
   # print(maze)
    return maze
    
#maze = createMaze(n) # stores maze in 2D Array format


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
    #Returns the coordinate of steps in maze
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



def getcolor(row,col,maze):
    #Decides color of square depedning on current value of 2D arrray
    currentsquareOnMaze =  maze[row][col]
    color = ()
    if currentsquareOnMaze == " ": 
        color = WHITE              #Empty space
    elif currentsquareOnMaze == "#":
        color = BLACK              #Obstracle
    elif currentsquareOnMaze == "0":
        color =  BLUE              #Starting point
    elif currentsquareOnMaze == "x":
        color = RED                #Finale desnination point
    else:               
        print("ERROR in @def getcolor : unable to deterimine color of square - " , '"'+currentsquareOnMaze+'"')
    return color
        
        
def draw_maze(screen,rowCount,colCount,SQUARESIZE,maze):
    #Convert 2d Array int0 maze
    
    #print(SQUARESIZE)
    for row in range(rowCount):
        for col in range(0,colCount):
            pygame.draw.rect(screen,getcolor(row, col,maze),(col*SQUARESIZE ,row*SQUARESIZE,SQUARESIZE-1,SQUARESIZE-1))
        
def get_newSquareColor(currentPos,SQUARESIZE,relativeColorChange = False):
    
    pixelPos = (math.floor((currentPos[1])*SQUARESIZE)+2,math.floor((currentPos[0])*SQUARESIZE)+2)
    if relativeColorChange:
        color = list(screen.get_at(pixelPos)) #change color of square relative to previosu color of square
    else:
        #change color of square independent to previosu color of square
        color = [random.randint(200,250),random.randint(100,250),random.randint(50,250)]
    
    #print(((currentPos[1]+5)*SQUARESIZE,(currentPos[0]+5)*SQUARESIZE))
    
    if(color[1]>minColor):
        color[1] -=colorDecreaseValue
    elif(color[0]>minColor):
        color[0] -= colorDecreaseValue
    elif(color[2] >minColor):
        color[2] -= colorDecreaseValue
    return color

s = 0 # counts the no. of loop executed 
def draw_sqaure(screen,path,startPos,SQUARESIZE,maze):
    #Change color of square once program steps on it
    global s 
    currentPos =  getCurrentPos(maze, startPos, path[s])
    color =  get_newSquareColor(currentPos,SQUARESIZE,relativeColorChange)
   # print((currentPos[1],currentPos[0]))
    pygame.draw.rect(screen,color,(currentPos[1]*SQUARESIZE ,currentPos[0]*SQUARESIZE,SQUARESIZE-1,SQUARESIZE-1))
    s +=1
    
def draw_square_short_path(screen,path,SQUARESIZE,maze):
    #Colors the given path green
    d = ""
    for i in path:
        #The method pick up last element of path array which is aLSO SHORTEST path of maze and paints it green
        d += i
        currentPos =  getCurrentPos(maze, findStart(maze),d)
        
        pygame.draw.rect(screen,GREEN,(currentPos[1]*SQUARESIZE ,currentPos[0]*SQUARESIZE,SQUARESIZE-1,SQUARESIZE-1))
        pygame.display.update()

def animateMazeSolving(screen,path,shortestPath,startpath,SQUARESIZE,maze):
        if s < len(path):
            draw_sqaure(screen,path,startpath,SQUARESIZE,maze)
        else:
            draw_square_short_path(screen,shortestPath,SQUARESIZE,maze)
            pygame.display.update()
            
            #pygame.quit()
def drawMaze(n,drawMaze = 1):
    maze = []
    
    if drawMaze == 1:
        maze =createEmptyMaze(n)
    elif drawMaze == 2:
        m = mazeClass(mazeName)
        maze = m.extractMaze()
    elif drawMaze == 3:
        print("Genrating a random maze IT will take some time Please wait")
        maze = random_maze(width = w,height = h,complexity = c,density = d)
        print("Random maze genrated!Please declare start and goal point")
    return maze
       
def solvemaze(maze,n):
    if n ==0:
        return BFSMain(maze)
    if n ==1:
        return AStarMain(maze)
screen = pygame.display.set_mode(screenSize)

#pygame.time.set_timer(drawEvent, t) # slows down the program do not use with low value of t
def main():
    maze = drawMaze(n,drawMazeOption) 
    rowCount = len(maze)
    colCount = len(maze[0])
    SQUARESIZE =  width/colCount
    startPos =  None
    pygame.init()
    
    isRunning = True
    screen.fill(WHITE) #Background color of maze 
   
    path = []
    shortPath = []
    draw_maze(screen,rowCount,colCount,SQUARESIZE,maze)
    pygame.display.update()
    #print("No. of turns -",s)
    print("genrating a maze")
    print("will start solving maze in few seconds")
    #time.sleep(waitTime)
    print("Starting to  solve the maze")
    solvingmaze = False
    solveMaze = False
    while isRunning:
        if solvingmaze:
            animateMazeSolving(screen,path,shortPath,startPos,SQUARESIZE,maze)
        pygame.display.update()
        for event  in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Executing quit command .")
                isRunning = False
                sys.exit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s  :
                    name = input("Enter name  of your maze \n")
                    
                    m = mazeClass(name)
                    m.saveMaze(maze)
                    
                    
            if solvingmaze and solveMaze :
                continue # Disable user control(below this if block)
            if pygame.mouse.get_pressed()[0] and not solveMaze :
                
                
                clickpos = pygame.mouse.get_pos()
                    
                row = math.floor(clickpos[1]/SQUARESIZE)
                col = math.floor(clickpos[0]/SQUARESIZE)
                if findStart(maze)[0] == -1 or  findStart(maze)[1] == -1:
                    maze[row][col] = "0"
                elif findEnd(maze)[0] == -1 or  findEnd(maze)[1] == -1:
                    maze[row][col] = "x"    
                else:
                    maze[row][col] = "#"
                pygame.draw.rect(screen,getcolor(row, col,maze),(col*SQUARESIZE ,row*SQUARESIZE,SQUARESIZE-1,SQUARESIZE-1))
                    #print(maze)
                    
                draw_maze(screen,row,col,SQUARESIZE,maze)
            if pygame.mouse.get_pressed()[2] :
                  #Remove object
                  clickpos = pygame.mouse.get_pos()
                  
                  row = math.floor(clickpos[1]/SQUARESIZE)
                  col = math.floor(clickpos[0]/SQUARESIZE)
                  maze[row][col] = " "
                  pygame.draw.rect(screen,getcolor(row, col,maze),(col*SQUARESIZE ,row*SQUARESIZE,SQUARESIZE-1,SQUARESIZE-1))
                  
                
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE:
                    if not solveMaze:
                        shortPath,path = solvemaze(maze,searchChoice)
                        startPos = findStart(maze)
                    #for m in maze:
                    #    print("".join(m))
                    #print(path)
                    solveMaze = True
                    solvingmaze = True
                if event.key == pygame.K_p and not solveMaze:
                    shortPath,path = solvemaze(maze,searchChoice)
                    startPos = findStart(maze)
                    solveMaze = True
                  
                
        
                
    
    pygame.quit()
    sys.exit          
    
    

main()
