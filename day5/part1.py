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

hashSet = set()
duplicateSet = set()
for coord in hasVent:
    if (tuple([coord[0], coord[1]]) in hashSet):
        duplicateSet.add(tuple([coord[0], coord[1]]))
    hashSet.add(tuple([coord[0], coord[1]]))

print(len(duplicateSet))
