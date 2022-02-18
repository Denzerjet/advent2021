input = open("input.txt", "r").read().splitlines()

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
        if (y1 > y2):
            y3 = y2
            while (y3 <= y1):
                hasVent.append([x1,y3])
                y3 += 1
        else:
            for y in range (y1, y2+1):
                hasVent.append([x1,y])

    if y1 == y2:
        if (x1 > x2):
            x3 = x2
            while (x3 <= x1):
                hasVent.append([x3,y1])
                x3 +=1
        else: 
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
embedded_counter = 0

#tupleList = tuple(coord for coord in hasVent)
#setList = set()
#for coord in hasVent:
#    setList.update(coord)

for coord in hasVent:
    xCoord = int(coord[0])
    yCoord = int(coord[1])
    #print("Outside coord: " + str(coord))
    for coordEmbedded in hasVent:
        if (counter == embedded_counter):
            samex = 0
            samey = 0
            embedded_counter += 1
            continue
        print("Embedded coord: " + str(coordEmbedded))
        if (xCoord == coordEmbedded[0]):
            samex = 1
        if (yCoord == coordEmbedded[1]):
            samey = 1
        if (samex == 1 and samey == 1):
            #print("hi")
            if (tuple(xCoord, yCoord) in repeat):
                pass
            else:
                count = count + 1
                repeat.append([xCoord,yCoord])
        samex = 0
        samey = 0
        embedded_counter += 1
    embedded_counter = 0
    counter += 1
    
print("Count: " + str(count))
