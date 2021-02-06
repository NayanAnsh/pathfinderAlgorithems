import os
     
class maze:
    FILEPATH = "E:\python programs\pathfinderAlgorithems\maze"
    def __init__(self,name):
        self.maze = maze
        self.name = name
        self.fileName = str(self.name)+".txt"
    def extractMaze(self):
        
        
        path = self.FILEPATH+ r"\\"+ self.fileName
        
        
        file =  open(path,"r")
        
        maze = []
        for line in file:
            maze.append(list(line.replace("\n", "")))
        return maze
    def isDuplicatefile(self,filename):
        
        
        listDir = os.listdir(self.FILEPATH)
        isDuplicate =  False
        for dirFileName in listDir:
             if dirFileName == filename:
                 isDuplicate = True
        return isDuplicate
   
    def saveMaze(self,maze):
        filename = self.fileName
        while(self.isDuplicatefile(filename)):
            filename = filename[:filename.find(".")] + "1"+".txt"
        path = self.FILEPATH+ r"\\"+ filename
        file = open(path,"a")
        for m in maze:
           file.write("".join(m)+"\n")
        print("maze saved as file -",filename)
        file.close()

