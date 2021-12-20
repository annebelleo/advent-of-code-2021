content_list = open("day3.txt", "r").read().splitlines()
# part 1
looper = 0  # position in string
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
sample_table = ["00100", "11110", "10110", "10111", "10101",
                "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
o2_rating = content_list.copy()
co2_rating = content_list.copy()
o2_remove = []
co2_remove = []
looper = 0
while looper < 12 and len(o2_rating) > 1:
    ones = 0
    zeros = 0
    # remove if not most common in position (keep 1 if equal)
    for binary in o2_rating:
        if binary[looper] == '0':
            zeros += 1
        elif binary[looper] == '1':
            ones += 1
    for i in range(0, len(o2_rating)):
        if (o2_rating[i][looper] == '1' and zeros > ones) or (o2_rating[i][looper] == '0' and ones >= zeros):
            o2_remove.append(o2_rating[i])
    for i in range(0, len(o2_remove)):
        if o2_remove[i] in o2_rating:
            o2_rating.remove(o2_remove[i])
    looper += 1

looper = 0
while looper < 12 and len(co2_rating) > 1:
    ones = 0
    zeros = 0
    for binary in co2_rating:
        if binary[looper] == '0':
            zeros += 1
        elif binary[looper] == '1':
            ones += 1
    print(looper, zeros, ones)
    for i in range(0, len(co2_rating)):
        if (co2_rating[i][looper] == '0' and zeros > ones) or (co2_rating[i][looper] == '1' and ones >= zeros):
            co2_remove.append(co2_rating[i])
    for i in range(0, len(co2_remove)):
        if co2_remove[i] in co2_rating:
            co2_rating.remove(co2_remove[i])
    looper += 1
print(o2_rating, co2_rating)
print(int(o2_rating[0], 2) * int(co2_rating[0], 2))
