import queue

#ToDo: put a input checker so that program do not take input of rows greater than n

def createMazeCode():
    n = int(input("Enter(Integer only) your maze dimension nxn "));
    code = "maze = [] \n"
    for i in range(n):
        print("Enter maze row --> ")
        s = input("-"*n +"\n");    
        code = code + "maze.append(["
        for j in list(s):
            code +=  '"' + j +'",'
        code = code[:len(code)-1] #Removing extra comma
        code  += "]) \n"

    print(code)
            
    return None;
createMazeCode()