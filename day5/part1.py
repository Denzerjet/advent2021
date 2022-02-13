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
        for y in range (y1, y2+1):
            hasVent.append([x1,y])

    if y1 == y2:
        for x in range (x1, x2+1):
            hasVent.append([y1,x])
    

count = 0
first = 0
samex = 0
samey = 0
xCoord = hasVent[0][0]
yCoord = hasVent[0][1]
repeat = []
for coord in hasVent:
    if (first == 0):
        first = 1
        continue
    if (xCoord == coord[0]):
        samex = 1
    if (yCoord == coord[1]):
        samey = 1
    
    if (samex == 1 and samey == 1):
        if ([xCoord, yCoord] in repeat):
            pass
        else:
            count = count + 1
            repeat.append[xCoord,yCoord]
    
    samex = 0
    samey = 0
    xCoord = coord[0]
    yCoord = coord[1]
    
print("Count: " + str(count))
