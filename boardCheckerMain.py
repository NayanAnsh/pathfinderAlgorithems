import pygame
import sys
import time
import math
import random
from BreadthFirstSearch.BreadthFirstSearchAlgorithem import createMaze, main as BFSMain
#Variable for user to control
n = 11# n is dimension of maze nxn # Only 3 5 10 as argument of main func is valid
minColor = 80 # minimum color value of rgb  allowed 
colorDecreaseValue = 20 # amount of color valueto decrease from r g b when program steps on same square
relativeColorChange =  False # if true then squares will chnage its color relative to its previous color
waitTime = 1 # wait time before start solving the maze
screenSize = width,height = 1000,1000 # dimension of window




#print(screenSize)

#Colors Constant
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE =  (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)

#Global variables
maze = createMaze(n) # stores maze in 2D Array format
rowCount = len(maze)
colCount = len(maze[0])
SQUARESIZE =  width/colCount


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
startPos =  findStart(maze)

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



def getcolor(row,col):
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
        
        
def draw_maze(screen):
    #Convert 2d Array int0 maze
    
    #print(SQUARESIZE)
    for row in range(rowCount):
        for col in range(0,colCount):
            pygame.draw.rect(screen,getcolor(row, col),(col*SQUARESIZE ,row*SQUARESIZE,SQUARESIZE-1,SQUARESIZE-1))
def get_newSquareColor(currentPos,relativeColorChange = False):
    pixelPos = (math.floor((currentPos[1])*SQUARESIZE)+5,math.floor((currentPos[0])*SQUARESIZE)+5)
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
def draw_sqaure(screen,path):
    #Change color of square once program steps on it
    global s 
    currentPos =  getCurrentPos(maze, startPos, path[s])
    color =  get_newSquareColor(currentPos,relativeColorChange)
    pygame.draw.rect(screen,color,(currentPos[1]*SQUARESIZE ,currentPos[0]*SQUARESIZE,SQUARESIZE-1,SQUARESIZE-1))
    s +=1
    
def draw_square_short_path(screen,path):
    #Colors the given path green
    d = ""
    for i in path[len(path)-1]:
        #The method pick up last element of path array which is aLSO SHORTEST path of maze and paints it green
        d += i
        currentPos =  getCurrentPos(maze, findStart(maze),d)
        
        pygame.draw.rect(screen,GREEN,(currentPos[1]*SQUARESIZE ,currentPos[0]*SQUARESIZE,SQUARESIZE-1,SQUARESIZE-1))
        

def animateMazeSolving(screen,path):
        if s < len(path):
            draw_sqaure(screen,path)
        else:
            draw_square_short_path(screen,path)
            pygame.display.update()
            
            #pygame.quit()
screen = pygame.display.set_mode(screenSize)
#pygame.time.set_timer(drawEvent, t) # slows down the program do not use with low value of t
def main():
    shortPath,path = BFSMain(n) 
    pygame.init()
    
    isRunning = True
    screen.fill(WHITE) #Background color of maze 
   
    
    draw_maze(screen)
    pygame.display.update()
    #print("No. of turns -",s)
    print("genrating a maze")
    print("will start solving maze in few seconds")
    time.sleep(waitTime)
    print("Starting to  solve the maze")
    while isRunning:
        animateMazeSolving(screen,path)
        pygame.display.update()
        for event  in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Executing quit command .")
                isRunning = False
                sys.exit
            
                  
                
        
                
    
    pygame.quit()
    sys.exit          
    
    

main()
