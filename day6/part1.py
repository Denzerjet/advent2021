input = open("input.txt", "r").read()
input_numbers = input.split(",")

gen = () #tuple 
for num in input_numbers:
    gen = gen + (int(num),) #have to use comma or else it isn't iterable 
