from turtle import pos


input = open("input.txt", "r").read()
positions = input.split(",")

min_sum = 0
sum_iterator = 0
max_pos = int(positions[0])

for crab_pos in positions:
    if(int(crab_pos) > max_pos):
        max_pos = int(crab_pos)

#store the smallest sum only
for i in range (max_pos):
    for crab_pos in positions:
        #n(n+1)/2 is closed form of the summation from 1 to n of i
        n = abs(i - int(crab_pos))
        sum_iterator += n*(n+1)/2
        #sum_iterator += abs(i - int(crab_pos))
    if (i==0):
        min_sum = sum_iterator
    if ((i!=0) and (min_sum > sum_iterator)):
        min_sum = sum_iterator
    sum_iterator = 0
print(min_sum)
