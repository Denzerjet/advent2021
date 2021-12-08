def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words

depths = readFile("depths.txt")

increases = 0
place = 0

while place < len(depths):
    if (place+3 < len(depths)):
        #print(place)
        #rint(int(depths[place]))
        arrayOne = [depths[place], depths[place+1], depths[place+2]]
        arrayTwo = [depths[place+1], depths[place+2], depths[place+3]]

        arraySumOne = 0
        arraySumTwo = 0

        for j in arrayOne:
            arraySumOne += int(j)
        for k in arrayTwo:
            arraySumTwo += int(k)

        if (arraySumOne < arraySumTwo):
            increases += 1
    place += 1

print(increases)