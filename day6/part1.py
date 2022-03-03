input = open("input.txt", "r").read()
input_numbers = input.split(",")

gen = () #tuple 
lantern_fish = []

for num in input_numbers:
    lantern_fish.append(int(num))

for fish in lantern_fish:
        print(fish)
for i in range (80):
    for j in range(len(lantern_fish)):
        if (lantern_fish[j] == 0):
            lantern_fish[j] = 6
            lantern_fish.append(8)
        else:
            lantern_fish[j] -= 1
print(len(lantern_fish))
