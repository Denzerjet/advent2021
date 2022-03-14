input = open("input.txt", "r").read().splitlines()

length = 0
inputTuple = tuple(tuple(i) for i in input)
sum = 0

#outer refers to each line of the input being stored as a single tuple
#inner refers to each of the numbers of each line of the input being stored as singular tuples inside of a tuple
# that encompasses all of them (like a 2d array)

#note: have to iterate by a number in range (...) because we tuples can't be converted to ints for comparisons
for outer in range (0, len(inputTuple)):
    largest = True
    for inner in range(0, len(inputTuple[outer])):
        #have a variable here and make all the following if statements nots, then
        #make a comparison to the right to the right (inner + 1) if inner != len(inputTuple[outer]) - 1
        #set the variable to false if it isn't the largest to it's adjacents
        #if the variable is true add it plus one to sum
        if (inner != 0):
            #if not on the left edge, compare to an element on the left
            largest = inputTuple[outer][inner] < inputTuple[outer][inner + 1]
        if (inner =! len(inputTuple[outer]) - 1):
            #if not on the right edge, compare to an element 
            pass
        if (outer == 0):
            #top edge
            pass
        if (outer == len(inputTuple) - 1):
            #bottom edge
            pass
        if (largest):
            #add it plus one to sum
            pass
