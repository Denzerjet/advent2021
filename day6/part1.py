input = open("input.txt", "r").read()
input_numbers = input.split(",")

gen = () #tuple 
lantern_fish = []

for num in input_numbers:
    lantern_fish.append(int(num))

for i in range (80):
    for j in len(lantern_fish):
        if (lantern_fish[i] == 0):
            lantern_fish[i] = 6
            lantern_fish.append(8)
        else:
            lantern_fish[i] -= 1
