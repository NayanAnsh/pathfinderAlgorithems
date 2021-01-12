file =  open("E:\python programs\pathfinderAlgorithems\BreadthFirstSearch\maze001.txt","r")
maze = []
for line in file:
    maze.append(list(line.replace("\n", "")))
for i in maze:
    print(i)