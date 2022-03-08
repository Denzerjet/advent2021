from pickle import TRUE
from tkinter import FALSE
from numpy import true_divide


def contains(code, number):
    #code is the unidentified code
    code_set = set(list(code))
    #number is a code whose corresponding num has been identified
    number_set = set(list(number))

    return number_set.issubset(code_set)

def containshalf(code, number):
    code_set = set(list(code))
    number_set = set(list(number))
    length = len(code_set.intersection(number_set))
    if (length == 2):
        return TRUE
    return FALSE

def equivalent(code, number):
    code_set = set(list(code))
    number_set = set(list(number))
    length = len(code_set.intersection(number_set))
    
    if (length == len(number_set) and length == len(code_set)):
        return True
    return False


input = open("input.txt", "r").read().splitlines()

#strings of each number
one = ""
four = ""
seven = ""
eight = ""

zero = ""
two = ""
three = ""
five = ""
six = ""
nine = ""

#now we find out the values for each part
#output_array is a terrible name 
sum = 0
line_number = 1
for line in input:
    output = line.split(" | ")
    output_array = output[0].split(" ")

    #Sets strings to their letter correspondants then breaks
    for number in output_array:
        if (len(number) == 2):
            one = number
        if (len(number) == 4):
            four = number
        if (len(number) == 3):
            seven = number
        if (len(number) == 7):
            eight = number
        if ((len(one) != 0) and (len(four) != 0) and (len(seven) != 0) and (len(eight) != 0)):
            break

    #print(zero)
    #print(one)
    #print(two)
    #print(three)
    #print(four)
    #print(five)
    #print(six)
    #print(seven)
    #print(eight)
    #print(nine)

    #print("######blah######")
    

    for number in output_array:
        if (contains(number, one) and len(number) == 6 and contains(number, four)):
            nine = number
        elif (contains(number, one) and contains(number, seven) and len(number) == 6):
            zero = number
        elif (contains(number, one) and contains(number, seven) and len(number) == 5):
            three = number
        elif (len(number) == 5 and containshalf(number, four)): 
            two = number
        elif (len(number) == 5):
            #TODO: implement function that caluclates if something is .75 (3/4ths) of something else (may not be necessary)
            five = number
        elif (len(number) == 6):
            six = number 
        

    #print(zero)
    #print(one)
    #print(two)
    #print(three)
    #print(four)
    #print(five)
    #print("six: " + str(six))
    #print(seven)
    #print(eight)
    #print("nine: " + str(nine))

    #then here you just sum the digits of the code after the | using the deciphered values you just calc'd above
    #and print the sum
    codes = output[1].split(" ")
    #these are the digits that the computer is trying to convey to the user
    digits = ""
    
    for code in codes:
        if (equivalent(code, zero)):
            digits += "0"
        if (equivalent(code, one)):
            digits += "1"
        elif (equivalent(code, two)):
            digits += "2"
        if (equivalent(code, three)):
            digits += "3"
        elif (equivalent(code, four)):
            digits += "4"
        if (equivalent(code, five)):
            digits += "5"
        elif (equivalent(code, six)):
            digits += "6"
        if (equivalent(code, seven)):
            digits += "7"
        elif (equivalent(code, eight)):
            digits += "8"
        if (equivalent(code, nine)):
            digits += "9"
    
    line_number += 1
    print(digits)
    sum += int(digits)
    one = ""
    four = ""
    seven = ""
    eight = ""

    zero = ""
    two = ""
    three = ""
    five = ""
    six = ""
    nine = ""


print("sum: " + str(sum))
