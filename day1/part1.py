def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words

depths = readFile("depths.txt")

increases = 0
old = -1

for i in depths:
    if old != -1:
        if old < int(i):
            increases += 1
    old = int(i)

print(increases)