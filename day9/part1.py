input = open("input.txt", "r").read().splitlines()

length = 0
inputTuple = tuple(tuple(i) for i in input)
sum = 0

for outer in range (0, len(inputTuple)):
    largest = True
    for inner in range(0, len(inputTuple[outer])):
        #have a variable here and make all the following if statements nots, then
        #make a comparison to the right to the right (inner + 1) if inner != len(inputTuple[outer]) - 1
        #set the variable to false if it isn't the largest to it's adjacents
        #if the variable is true add it plus one to sum
        if (inner != 0 and inner != len(inputTuple[outer]) - 1):
            #if not on the left edge
            largest = inputTuple[outer][inner] < inputTuple[outer][inner + 1]
            pass
        elif (inner =! len(inputTuple[outer]) - 1):
            #if not on the right edge
            pass
        if (outer == 0):
            #top edge
            pass
        elif (outer == len(inputTuple) - 1):
            #bottom edge
            pass

        if (largest):
            #add it plus one to sum
            pass
