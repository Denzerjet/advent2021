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
            arr = arr + [[outer],[inner]]

# plan: go through each marked coordinant and iterate out from there to count out the size of its "region"
# have an array of 3 elements, for each coordinate's regional size compare to lowest element in array and replace if greater
print(arr)
