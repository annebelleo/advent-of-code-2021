content_list = open("day3.txt", "r").read().splitlines()
# part 1
looper = 0
gamma = ""
epsilon = ""

while looper < 12:  # number of digits in the binary numbers given
    ones = 0
    zeros = 0
    for binary in content_list:  # each string in list
        if binary[looper] == '0':
            zeros += 1
        elif binary[looper] == '1':
            ones += 1
    if zeros > ones:
        gamma += '0'
        epsilon += '1'
    if ones > zeros:
        gamma += '1'
        epsilon += '0'
    looper += 1
print(int(gamma, 2) * int(epsilon, 2))
# part 2
