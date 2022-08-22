input = open("input.txt", "r").read().splitlines()

inputTuple = tuple(tuple(i) for i in input)
sum = 0

#outer refers to each line of the input being stored as a single tuple
#inner refers to each of the numbers of each line of the input being stored as singular tuples inside of a tuple
# that encompasses all of them (like a 2d array)

#note: have to iterate by a number in range (...) because we tuples can't be converted to ints for comparisons
for outer in range (0, len(inputTuple)):
    smallest = 0
    for inner in range(0, len(inputTuple[outer])):
        #have a variable here and make all the following if statements nots, then
        #make a comparison to the right to the right (inner + 1) if inner != len(inputTuple[outer]) - 1
        #set the variable to false if it isn't the largest to it's adjacents
        #if the variable is true add it plus one to sum
        if (inner != 0):
            #if not on the left edge, compare to an element on the left
            ##print("Outer: " + str(outer))
            ##print("Inner: " + str(inner))
            ##print("First num: " + inputTuple[outer][inner])
            ##print("Second num: " + inputTuple[outer][inner - 1])
            smallest = inputTuple[outer][inner] < inputTuple[outer][inner - 1]
        if ((inner != len(inputTuple[outer]) - 1) and (smallest)):
            #if not on the right edge, compare to an element on the right
            smallest = inputTuple[outer][inner] < inputTuple[outer][inner + 1]
        if ((outer != 0) and (smallest)):
            #not top edge
            smallest = inputTuple[outer][inner] < inputTuple[outer - 1][inner]
        if ((outer != len(inputTuple) - 1) and (smallest)):
            #not bottom edge
            smallest = inputTuple[outer][inner] < inputTuple[outer + 1][inner]
        if (smallest):
            #add it plus one to sum
            #print("Outer: " + str(outer))
            #print("Inner: " + str(inner))
            #print(inputTuple[outer][inner])
            sum += 1 + int(inputTuple[outer][inner])


print("Sum: " + str(sum))
