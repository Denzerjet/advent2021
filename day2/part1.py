words = open("input.txt", "r").read().splitlines()

x = 0
y = 0

for i in words:
    instruction = i.split(" ", 2)
    direction = instruction[0]
    magnitude = instruction[1]

    if direction == "forward":
        x += int(magnitude)
    if direction == "down":
        y += int(magnitude)
    if direction == "up":
        y -= int(magnitude)

result = x * y

print(result)

