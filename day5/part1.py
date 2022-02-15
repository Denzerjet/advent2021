input = open("testinput.txt", "r").read().splitlines()


#MISTAKE: I ONLY ADD VENTS TO hasVent WHICH ARE FROM x1,y2 to x2,y2 when x2> x1 and y2>y1 
#need to evaluate which way the vent vector points and record that correspondinly
hasVent = []
for i in input:
    firstHalf = i.split("->")[0]
    secondHalf = i.split("->")[1]

    firstHalf = firstHalf.replace(" ", "")
    secondHalf = secondHalf.replace(" ", "")

    x1 = int(firstHalf.split(",")[0])
    y1 = int(firstHalf.split(",")[1])

    x2 = int(secondHalf.split(",")[0])
    y2 = int(secondHalf.split(",")[1])

    if x1 == x2:
        for y in range (y1, y2+1):
            hasVent.append([x1,y])

    if y1 == y2:
        for x in range (x1, x2+1):
            hasVent.append([x,y1])

count = 0
first = 0
samex = 0
samey = 0
xCoord = int(hasVent[0][0])
yCoord = int(hasVent[0][1])
repeat = []
counter = 0
for coord in hasVent:
    xCoord = int(coord[0])
    yCoord = int(coord[1])
    print("Outside coord: " + str(coord))
    hasVent.remove(coord)
    for coordEmbedded in hasVent:
        #print("Embedded coord: " + str(coordEmbedded))
        if (xCoord == coordEmbedded[0]):
            samex = 1
        if (yCoord == coordEmbedded[1]):
            samey = 1
        if (samex == 1 and samey == 1):
            print("hi")
            if ([xCoord, yCoord] in repeat):
                pass
            else:
                count = count + 1
                repeat.append([xCoord,yCoord])
        samex = 0
        samey = 0
    hasVent.insert(counter, coord)
    counter += 1
    
print("Count: " + str(count))
