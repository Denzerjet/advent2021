input = open("input.txt", "r").read()
input_numbers = input.split(",")

num_0 = 0
num_1 = 0
num_2 = 0
num_3 = 0
num_4 = 0
num_5 = 0
num_6 = 0
num_7 = 0
num_8 = 0

for num in input_numbers:
    if (int(num) == 0):
        num_0 += 1 
    if (int(num) == 1):
        num_1 += 1
    if (int(num) == 2):
        num_2 += 1
    if (int(num) == 3):
        num_3 += 1
    if (int(num) == 4):
        num_4 += 1
    if (int(num) == 5):
        num_5 += 1
    if (int(num) == 6):
        num_6 += 1
    if (int(num) == 7):
        num_7 += 1
    if (int(num) == 8):
        num_8 += 1

temp_0 = 0
temp_1 = 0
temp_2 = 0
temp_3 = 0
temp_4 = 0
temp_5 = 0
temp_6 = 0
temp_7 = 0
temp_8 = 0

for i in range (256):
    temp_8 += num_0
    temp_6 += num_0
    num_0 -= num_0
    num_0 += num_1
    num_1 -= num_1
    temp_1 += num_2
    num_2 -= num_2
    temp_2 += num_3
    num_3 -= num_3
    temp_3 += num_4
    num_4 -= num_4
    temp_4 += num_5
    num_5 -= num_5
    temp_5 += num_6
    num_6 -= num_6
    temp_6 += num_7
    num_7 -= num_7
    temp_7 += num_8
    num_8 -= num_8
    num_0 += temp_0
    num_1 += temp_1
    num_2 += temp_2
    num_3 += temp_3
    num_4 += temp_4
    num_5 += temp_5
    num_6 += temp_6
    num_7 += temp_7
    num_8 += temp_8
    temp_0 = 0
    temp_1 = 0
    temp_2 = 0
    temp_3 = 0
    temp_4 = 0
    temp_5 = 0
    temp_6 = 0
    temp_7 = 0
    temp_8 = 0

sum = num_0 + num_1 + num_2 + num_3 + num_4 + num_5 + num_6 + num_7 + num_8
print(sum)
