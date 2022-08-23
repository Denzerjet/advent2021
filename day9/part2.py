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

for outer in range (0, len(inputTuple)):
    for inner in range(0, len(inputTuple[outer])):

