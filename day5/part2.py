import math

input = open("testinput.txt", "r").read().splitlines()

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
    else:
        if (y2 > y1):
            x3 = max(x1,x2) - min(x1,x2)
            k = 0
            while (k <= x3):
                hasVent.append([min(x1,x2)+k,min(y1,y2)+k])
                k += 1
        else:
            x3 = abs(max(x1,x2) - min(x1,x2))
            k = 0
            if (x2 > x1 and y2 > y1):
                while (k <= x3):
                    hasVent.append([x1+k,y1+k])
                    k += 1
            if (x2 > x1 and y1 > y2):
                while (k <= x3):
                    hasVent.append([x1+k,y1-k])
                    k += 1
            if (x1 > x2 and y2 > y1):
                while (k <= x3):
                    hasVent.append([x2+k,y2-k])
                    k += 1
            if (x1 > x2 and y1 > y2):
                while (k <= x3):
                    hasVent.append([x2+k,y2+k])
                    k += 1

for coord in hasVent:
    print(coord)

hashSet = set()
duplicateSet = set()
for coord in hasVent:
    if (tuple([coord[0], coord[1]]) in hashSet):
        duplicateSet.add(tuple([coord[0], coord[1]]))
    hashSet.add(tuple((coord[0], coord[1])))

print(len(duplicateSet))
