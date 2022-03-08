def contains(code, number):
    #code is the unidentified code
    code_set = set(list(code))
    #number is a code whose corresponding num has been identified
    number_set = set(list(number))

    return number_set.issubset(code_set)

def containshalf(code, number):
    code_set = set(list(code))
    print(code_set)
    number_set = set(list(number))
    print(number_set)
    length = len(code_set.intersection(number_set))
    print(code_set.intersection(number_set))
    print(length)
    if (length == 2):
        return True
    return False

def equivalent(code, number):
    code_set = set(list(code))
    number_set = set(list(number))
    length = len(code_set.intersection(number_set))
    print(length)
    print(len(number_set))
    print(len(code_set))
    
    if (length == len(number_set) and length == len(code_set)):
        return True
    return False

#contains_code = "hello"
#contains_number = "ho"
#print(contains(contains_code, contains_number))

#test = set('h','e','l','l','o')
#test = list(contains_code)
#for part in test:
#    print(part)

#half_code = "hound"
#half_number = "hzoz"
#print(containshalf(half_code, half_number))

#print(equivalent("ba", "ab"))

str = "0505"
print(int(str))
