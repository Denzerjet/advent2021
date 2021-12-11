input = open("input.txt", "r").read().splitlines()
divisor = 1000000000000 # change back later
j=0
oxygen_string = ""
carbondioxide_string = ""
oneCount = 0
zeroCount = 0
keepGoing = 1
oxygen_choice = ""

while (j < 12 and bool(keepGoing)): #change 5 to a 12 later
    for i in input:
        #print("i string: " + i[0:j])
        #print ("oxygen_string: " + oxygen_string)
        if i[0:j] == oxygen_string:
            oxygen_choice = i
            digit = int(i) % divisor
            #print("initial digit: " + str(digit))
            digit = digit / (divisor/10)
            #print("digit: " + str(digit))
            
            if (digit == 1):
                oneCount += 1
            if (digit == 0):
                zeroCount += 1
    
    if (oneCount + zeroCount > 1):
        if (oneCount > zeroCount):
            oxygen_string += str(1)
        if (zeroCount > oneCount):
            oxygen_string += str(0)
        if (zeroCount == oneCount):
            oxygen_string += str(1)
    else:
        keepGoing = 0

    divisor = divisor/10
    oneCount = 0
    zeroCount = 0
    j += 1

divisor = 1000000000000 # a 0 for each digit space
j=0
keepGoing = 1
carbon_choice = ""

while (j < 12 and bool(keepGoing)): #change 5 to a 12 later
    for i in input:
        print("i string: " + i[0:j])
        print ("carbondioxide_string: " + carbondioxide_string)
        if i[0:j] == carbondioxide_string:
            carbon_choice = i
            digit = int(i) % divisor
            digit = digit / (divisor/10)
            print("digit: " + str(digit))
            
            if (digit == 1):
                oneCount += 1
            if (digit == 0):
                zeroCount += 1

    if (oneCount + zeroCount > 1):
        if (oneCount < zeroCount):
            carbondioxide_string += str(1)
        if (zeroCount < oneCount):
            carbondioxide_string += str(0)
        if (zeroCount == oneCount):
            carbondioxide_string += str(0)
    else:
        keepGoing = 0

    divisor = divisor/10
    oneCount = 0
    zeroCount = 0
    j += 1


print ("oxygen_choice: " + oxygen_choice)
print("carbon_choice: " + carbon_choice)

oxygen_rating = int(oxygen_choice, 2)
carbondioxide_rating = int(carbon_choice, 2)

print("oxygen_rating: " + str(oxygen_rating))
print("carbondioxide_rating: " + str(carbondioxide_rating))

print(str(oxygen_rating * carbondioxide_rating))