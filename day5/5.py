content_list = open("day5.txt", "r").read().splitlines()
# build matrix
grid = [[0]*1000]*1000

# filter lines
wanted_lines = []

# read lines
for line in content_list:
    duples = line.split(" -> ")
    x1y1 = duples[0].split(',')
    x1y1 = [int(i) for i in x1y1]
    x2y2 = duples[1].split(',')
    x2y2 = [int(i) for i in x2y2]
    # only look at horizontal and vertical lines
    if x1y1[0] == x2y2[0] or x1y1[1] == x2y2[1]:
        wanted_lines.append([x1y1, x2y2])

# iterate over grid
print(wanted_lines)
for i in range(0, len(wanted_lines)):
    print("iteration: ", i)
    if wanted_lines[i][0] == wanted_lines[i+1][0]:
        print("x")
        # if x1 and x2 are the same
        for i in range(wanted_lines[i][1], wanted_lines[i+1][1]):
            grid[wanted_lines[i][1]][wanted_lines[i][0]] += 1
    elif wanted_lines[i][1] == wanted_lines[i+1][1]:
        print("y")
        # if y1 and y2 are the same
        for i in range(wanted_lines[i][0], wanted_lines[i+1][0]):
            grid[wanted_lines[i][1]][wanted_lines[i][0]] += 1
