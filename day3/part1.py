input = open("input.txt", "r").read().splitlines()
divisor = 10
j=0
gamma_string = ""
epsilon_string = ""
oneCount = 0
zeroCount = 0

while (j < 12):
    for i in input:
        digit = int(i) % divisor
        digit = digit / (divisor/10)
        if digit == 1:
            oneCount += 1
        elif digit == 0:
            zeroCount += 1

    if (oneCount > zeroCount):
        gamma_string = "1" + gamma_string
        epsilon_string = "0" + epsilon_string
    else:
        epsilon_string = "1" + epsilon_string
        gamma_string = "0" + gamma_string
    
    oneCount = 0
    zeroCount = 0
    divisor *= 10
    j += 1

print("Gamma string:" + gamma_string)
print("Epsilon string:" + epsilon_string)

epsilon = int(epsilon_string, 2)
gamma = int(gamma_string, 2)

print(gamma * epsilon)