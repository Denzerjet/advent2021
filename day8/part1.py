input = open("input.txt", "r").read().splitlines()

occurances = 0
for line in input:
    output = line.split(" | ")[1]
    output_array = output.split(" ")
    for number in output_array:
        if (len(number) == 2 or len(number) == 3 or len(number) == 4 or len(number) == 7):
            occurances += 1
print(occurances)
