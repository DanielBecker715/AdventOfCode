import hashlib
from collections import defaultdict

# Settings
inputPath = r'C:/Github-Projects/AdventOfCode/2022/Day7 - No Space Left On Device/input.in'

with open(inputPath, 'r', encoding="utf-8") as file:
    lines = file.readlines()

directory = defaultdict(int)
currentDirectory = []

for line in lines:
    line = line.rstrip()
    commandline = line.split(" ")

    if line[0] == "$":
        commandline.remove("$")
        
        print(line)
        if (commandline[0] == "cd"):
            if (commandline[1] == ".."):
                currentDirectory.pop()
                print("Switched to:", currentDirectory,"\n")
            else:
                currentDirectory.append(commandline[1])
                print("Switched to:", currentDirectory,"\n")
    #Ignore ls
    elif (commandline[0] == "ls"):
        continue
    #Ignore dir
    elif (commandline[0] == "dir"):
        continue
    else:
        sizeOfFile = int(commandline[0])
        print("Found file:",commandline)
        plainTextPath = "".join(currentDirectory)

        if (directory.get(plainTextPath) == None):
            directory[plainTextPath] = 0

        #Add the same size to each folder until the current folder is reached
        for i in range(1, len(currentDirectory)+1):
            directory[" ".join(currentDirectory[:i])] += sizeOfFile
        print("Path:", plainTextPath, directory[plainTextPath], "\n")

maxDiskSpace = 70000000
updateSize = 30000000
neededSpaceForUpdate = maxDiskSpace - updateSize
totalUsedDiskSpace = directory['/']

print("-- All Directories --")

part1=0
part2=1e9
for i,v in directory.items():
    print(i,v)
    if v <= 100000:
        part1 += v
    if v >= totalUsedDiskSpace-neededSpaceForUpdate:
        part2 = min(part2, v)

#print ("All directorys in dictionary:", directory)
print ("Part1:", part1, "Part2", part2)