import pygame
import sys
import time
import math
import random
from BreadthFirstSearch.BreadthFirstSearchAlgorithem import createMaze,main
n = 11 # n is dimension of maze nxn # Only 3 5 10 as argument of main func is valid
t = 1000 # time(in ms) between 2 consecutive steps #lower the time for faster result 
minColor = 80
colorDecreaseValue = 20
maze = createMaze(n)
stepMade = ""

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
shortPath,path = main(n)
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
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE =  (0,0,255)
RED = (255,0,0)
GREEN = (0,50,0)
screenSize = width,height = 1000,1000
FPS = 420 #Frame per second
rowCount = len(maze)
colCount = len(maze[0])
SQUARESIZE =  width/colCount
#print(screenSize)

def getcolor(row,col):
    currentsquareOnMaze =  maze[row][col]
    color = ()
    if currentsquareOnMaze == " ":
        color = WHITE
    elif currentsquareOnMaze == "#":
        color = BLACK
    elif currentsquareOnMaze == "0":
        color =  BLUE
    elif currentsquareOnMaze == "x":
        color = RED
    else:
        print("ERROR in @def getcolor : unable to deterimine color of square - " , '"'+currentsquareOnMaze+'"')
    return color
        
        
def draw_maze(screen):
    
    
    #print(SQUARESIZE)
    for row in range(rowCount):
        for col in range(0,colCount):
            pygame.draw.rect(screen,getcolor(row, col),(col*SQUARESIZE ,row*SQUARESIZE,SQUARESIZE-1,SQUARESIZE-1))
        
s = 0
startPos =  findStart(maze)
def draw_sqaure(screen):
    global stepMade
    global s
    currentPos =  getCurrentPos(maze, startPos, path[s])
    pixelPos = (math.floor((currentPos[1])*SQUARESIZE)+5,math.floor((currentPos[0])*SQUARESIZE)+5)
    color = list(screen.get_at(pixelPos)) #change color of square relative to previosu color of square
    #color = [random.randint(100,250),random.randint(100,250),random.randint(100,250)]#change color of square independent to previosu color of square
    #screen.set_at(pixelPos,(0,50,165))
    #print(((currentPos[1]+5)*SQUARESIZE,(currentPos[0]+5)*SQUARESIZE))
    
    if(color[1]>minColor):
        color[1] -=colorDecreaseValue
    elif(color[0]>minColor):
        color[0] -= colorDecreaseValue
    elif(color[2] >minColor):
        color[2] -= colorDecreaseValue
    
    pygame.draw.rect(screen,color,(currentPos[1]*SQUARESIZE ,currentPos[0]*SQUARESIZE,SQUARESIZE-1,SQUARESIZE-1))
    s +=1
    
def draw_square_short_path(screen):
    d = ""
    for i in path[len(path)-1]:
        d += i
        currentPos =  getCurrentPos(maze, findStart(maze),d)
        pygame.draw.rect(screen,[0,255,0],(currentPos[1]*SQUARESIZE ,currentPos[0]*SQUARESIZE,SQUARESIZE-1,SQUARESIZE-1))
        
pygame.init()
screen = pygame.display.set_mode(screenSize)
drawEvent = pygame.USEREVENT+1

#pygame.time.set_timer(drawEvent, t)
def main():
    isRunning = True
    screen.fill(WHITE) #Background color of maze 
    #clock = pygame.time.Clock()
    
    draw_maze(screen)
    pygame.display.update()
    #print("No. of turns -",s)
    print("genrating a maze")
    print("will start solving maze in few seconds")
    time.sleep(5)
    print("Starting to  solve the maze")
    while isRunning:
        
        
     #   clock.tick(FPS)
        if s < len(path):
            draw_sqaure(screen)
        else:
            draw_square_short_path(screen)
            print("Total time in sec -",pygame.time.get_ticks()//1000)
            pygame.display.update()
            #pygame.quit()
        pygame.display.update()
        for event  in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Executing quit command .")
                isRunning = False
                sys.exit
            elif event.type == drawEvent:
                if s < len(path):
                    pass
                  #  draw_sqaure(screen)
                
        
                
    
    pygame.quit()
    sys.exit          
    
    

main()
