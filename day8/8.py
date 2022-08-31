content_list = open("day8.txt", "r").read().splitlines()

# part 1
# 1: c,f (2)
# 4: b,c,d,f (4)
# 7: a,c,f (3)
# 8: a,b,c,d,e,f,g (7)
sum = 0
for i in content_list:
    line = i.split(' | ')
    segment = line[1].split()
    for j in segment:
        if len(j) == 2 or len(j) == 3 or len(j) == 4 or len(j) == 7:
            sum += 1
print(sum)

# part 2 (WIP)
sum = 0
for i in content_list:
    output = ""
    list = ['','','','','','',''] # order of d,e,a,f,g,b,c as in example
    line = i.split(' | ')
    segment = line[1].split()
    for j in segment:
        print(j)
        value = 0
        if len(j) == 2:
            value = 1
            list[2] = j # list all possible letters belonging in space
            list[5] = j
        elif len(j) == 3:
            value = 7
            list[0] = j
            list[2] = j
            list[5] = j
        elif len(j) == 4:
            value = 4
            list[1] = j
            list[2] = j
            list[3] = j
            list[5] = j
        elif len(j) == 7:
            value = 8
            for index in range(len(list)):
                list[index] = j
        elif len(j) == 6:
            if list[5]:
                for substring in list[5]:
                    if substring not in j:
                        value = 9
                    else:
                        value = 6
        elif len(j) == 5:
            for substring in list[2]:
                if substring not in j:
                    value = 5
        print(list)
        output += str(value)
    # print(output)
    sum += int(output)
# print(sum)
