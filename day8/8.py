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
# print(sum)

# part 2

def myFunc(e):
    return len(e)


def two(word, list):
    value = 1
    list[2] = word
    list[5] = word
    return value


def three(word, list):
    value = 7
    for letter in word:
        if letter in list[2] and letter in list[5]:
            word = word.replace(letter, "")
        list[0] = word
    return value


def four(word, list):
    value = 4
    for letter in word:
        if letter in list[2] and letter in list[5]:
            word = word.replace(letter, "")
        list[1] = word
        list[3] = word
    return value


def five(word, list):
    counttwo = 0
    countfive = 0
    for letter in word:
        if letter in list[1]:
            countfive += 1
        elif letter in list[4]:
            counttwo += 1
    if counttwo > 1:
        value = 2
    elif countfive > 1:
        value = 5
    else:
        value = 3
    print(word, list, value)
    return value


def six(word, list):
    countzero = 0
    countsix = 0
    countnine = 0
    for letter in word:
        if letter in list[2]:
            countsix += 1
        elif letter in list[3]:
            countzero += 1
        elif letter in list[4]:
            countnine += 1
    if countzero < 2:
        value = 0
    elif countsix < 2:
        value = 6
    elif countnine < 2:
        value = 9
    return value


def seven(word, list):
    value = 8
    for letter in word:
        if letter in list[0]:
            word = word.replace(letter, "")
        elif letter in list[1] and letter in list[3]:
            word = word.replace(letter, "")
        elif letter in list[2] and letter in list[5]:
            word = word.replace(letter, "")
        list[4] = word
        list[6] = word
    return value


sum = 0
for i in content_list:
    output = ""
    sides = i.split(' | ')
    left = sides[0].split()
    left.sort(key=myFunc)
    right = sides[1].split()
    list = ['', '', '', '', '', '', '']  # order of d,e,a,f,g,b,c as in example
    for j in left:
        if len(j) == 2:
            two(j, list)
        elif len(j) == 3:
            three(j, list)
        elif len(j) == 4:
            four(j, list)
        elif len(j) == 7:
            seven(j, list)
    for k in right:
        if len(k) == 2:
            value = two(k, list)
        elif len(k) == 3:
            value = three(k, list)
        elif len(k) == 4:
            value = four(k, list)
        elif len(k) == 5:
            value = five(k, list)
        elif len(k) == 6:
            value = six(k, list)
        elif len(k) == 7:
            value = seven(k, list)
        output += str(value)
    sum += int(output)
print(sum)
