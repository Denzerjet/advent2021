words = open("input.txt", "r").read().splitlines()

x = 0
depth = 0
aim = 0

for i in words:
    instruction = i.split(" ", 2)
    direction = instruction[0]
    magnitude = int(instruction[1])

    if direction == "forward":
        x += magnitude
        depth += aim * magnitude
    if direction == "down":
        aim += magnitude
    if direction == "up":
        aim -= magnitude

result = x * depth

print(result)

