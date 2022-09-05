content_list = open("day9.txt", "r").read().splitlines()
risk_level = 0


def check_below(line, position):
    if int(content_list[line+1][position]) > int(content_list[line][position]):
        return True


def check_above(line, position):
    if int(content_list[line-1][position]) > int(content_list[line][position]):
        return True


def check_left(line, position):
    if int(content_list[line][position-1]) > int(content_list[line][position]):
        return True


def check_right(line, position):
    if int(content_list[line][position+1]) > int(content_list[line][position]):
        return True


for line in range(len(content_list)):
    for position in range(len(content_list[line])):
        if position == 0 and line == 0:  # top left
            if check_right(line, position) and check_below(line, position):
                risk_level += int(content_list[line][position]) + 1
        elif position == len(content_list[line]) - 1 and line == 0:  # top right
            if check_left(line, position) and check_below(line, position):
                risk_level += int(content_list[line][position]) + 1
        elif position == 0 and line == len(content_list) - 1:  # bottom left
            if check_right(line, position) and check_above(line, position):
                risk_level += int(content_list[line][position]) + 1
        elif position == len(content_list[line]) - 1 and line == len(content_list) - 1:
            if check_left(line, position) and check_above(line, position):
                risk_level += int(content_list[line][position]) + 1
        elif position == 0:
            if check_above(line, position) and check_right(line, position) and check_below(line, position):
                risk_level += int(content_list[line][position]) + 1
        elif position == len(content_list[line]) - 1:
            if check_above(line, position) and check_left(line, position) and check_below(line, position):
                risk_level += int(content_list[line][position]) + 1
        elif line == 0:
            if check_left(line, position) and check_right(line, position) and check_below(line, position):
                risk_level += int(content_list[line][position]) + 1
        elif line == len(content_list) - 1:
            if check_left(line, position) and check_right(line, position) and check_above(line, position):
                risk_level += int(content_list[line][position]) + 1
        else:
            if check_left(line, position) and check_right(line, position) and check_above(line, position) and check_below(line, position):
                risk_level += int(content_list[line][position]) + 1
print(risk_level)
