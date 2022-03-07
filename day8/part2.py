def contains(code, number):
    #code is the unidentified code
    code_set = set(code.split("(?!^)"))
    #number is a code whose corresponding num has been identified
    number_set = set(number.split("(?!^)"))

    return number_set.issubset(code_set)


input = open("input.txt", "r").read().splitlines()

#strings of each number
one = ""
four = ""
seven = ""
eight = ""

#Sets strings to their letter correspondants then breaks
for line in input:
    output = line.split(" | ")[1]
    output_array = output.split(" ")
    for number in output_array:
        if (len(number) == 2):
            one = number
        if (len(number) == 4):
            four = number
        if (len(number) == 3):
            seven = number
        if (len(number) == 7):
            eight = number
        if (len(one) != 0 and len(four) != 0 and len(seven) != 0 and len(eight != 0)):
            break
    if (len(one) != 0 and len(four) != 0 and len(seven) != 0 and len(eight != 0)):
            break

two = ""
three = ""
five = ""
six = ""
nine = ""

#now we find out the values for each part
occurances = 0
for line in input:
    output = line.split(" | ")[1]
    output_array = output.split(" ")
    for number in output_array:
        if (contains(number, one) and contains(number, seven) and len(number) == 6):
            zero = number
        if (contains(number, one) and contains(number, seven) and len(number) == 5):
            three = number
        elif (len(number == 5)): 
            #TODO: implement function that calculates if something contains one half (2/4ths) of something else
            two = number
        elif (len(number == 5)):
            #TODO: implement function that caluclates if something is .75 (3/4ths) of something else
            five = number
        if (contains(number, one) and len(number) == 6):
            nine = number
        elif (len(number == 6)):
            number = six
    #then here you just sum the digits of the code after the | using the deciphered values you just calc'd above
    #and print the sum

print(occurances)
