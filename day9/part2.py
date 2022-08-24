input = open("input.txt", "r").read().splitlines()

inputTuple = tuple(tuple(i) for i in input)
arr = []

for outer in range (0, len(inputTuple)):
    smallest = 0
    for inner in range(0, len(inputTuple[outer])):
        if (inner != 0):
            smallest = inputTuple[outer][inner] < inputTuple[outer][inner - 1]
        if ((inner != len(inputTuple[outer]) - 1) and (smallest)):
            smallest = inputTuple[outer][inner] < inputTuple[outer][inner + 1]
        if ((outer != 0) and (smallest)):
            smallest = inputTuple[outer][inner] < inputTuple[outer - 1][inner]
        if ((outer != len(inputTuple) - 1) and (smallest)):
            smallest = inputTuple[outer][inner] < inputTuple[outer + 1][inner]
        if (smallest):
            arr = arr + [[outer,inner]]

# plan: go through each marked coordinant and iterate out from there to count out the size of its "region"
# have an array of 3 elements, for each coordinate's regional size compare to lowest element in array and replace if greater

# above wouldn't work practically (trying to iterate out from each point to find it's regional mass)
# every point (excluding 9s) belongs exactly to one basin, go through the entire system of coords and for each one find out which basin it corresponds to
# then add a point to an array that stored each point as a hash value, or make an array of size of arr and just add 1 to the slot corresponding (# - 1) then 
# the end just multiply the largest numbers together

# store as hash, compare to hash, for index with matching add one to sizes

# I have realized that my part1 solution is not fully correct
sizes = [0] * len(arr)

comp = -1
compto = -1
dir = -1

x = -1
y = -1
# 0 1 2 3
for outer in range (0, len(inputTuple)):
    for inner in range(0, len(inputTuple[outer])):
        # if not a 9, consider for regional mass
        
        # check each direction, find the greatest difference, but if the end difference isnt positive then skip
        if (inputTuple[outer][inner] != 9):
            if (inner != 0):
                comp = inputTuple[outer][inner] - inputTuple[outer][inner - 1]
                dir = 0
            if (inner != len(inputTuple[outer]) - 1):
                compto = inputTuple[outer][inner] - inputTuple[outer][inner + 1]

                comp = min(comp, compto)

                if (comp == compto):
                    dir = 1
            if (outer != 0):
                compto = inputTuple[outer][inner] - inputTuple[outer - 1][inner]

                comp = min(comp, compto)

                if (comp == compto):
                    dir = 2
            if (outer != len(inputTuple) - 1):
                compto = inputTuple[outer][inner] - inputTuple[outer - 1][inner]

                comp = min(comp, compto)

                if (comp == compto):
                    dir = 3
            
            # if there was an adjacent (not including diagonals) square that water would flow to
            # would need to store outer and inner as x and y so that once you find the vent that a square corresponds to
            # you can then continue from the original square seeing as the or

            # revision: create function findVent() which goes through inputTuble and navigates to the corresponding vent
            if (comp > 0):
                if (dir == 0):
                    pass
                if (dir == 1):
                    pass
                if (dir == 2):
                    pass
                if (dir == 3):
                    pass
            else:
                # if we have navigated to the vent 
                pass

print(sizes)
