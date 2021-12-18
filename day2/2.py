# part 1
content_list = open("day2.txt", "r").read().splitlines()
directions = []
for i in content_list:
    words = i.split(' ')
    directions.append(words)

h_position = 0
depth = 0

for list in directions:
    if list[0] == 'forward':
        h_position += int(list[1])
    elif list[0] == 'down':
        depth += int(list[1])
    elif list[0] == 'up':
        depth -= int(list[1])
print(h_position*depth)
# part 2
h_position = 0
depth = 0
aim = 0

for list in directions:
    if list[0] == 'forward':
        h_position += int(list[1])
        depth += aim * int(list[1])
    if list[0] == 'down':
        aim += int(list[1])
    if list[0] == 'up':
        aim -= int(list[1])
print(h_position*depth)
