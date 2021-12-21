content_list = open("day5.txt", "r").read().splitlines()

sample_list = ['0,9 -> 5,9',
               '8,0 -> 0,8',
               '9,4 -> 3,4',
               '2,2 -> 2,1',
               '7,0 -> 7,4',
               '6,4 -> 2,0',
               '0,9 -> 2,9',
               '3,4 -> 1,4',
               '0,0 -> 8,8',
               '5,5 -> 8,2']

# build matrix
grid = []
for i in range(1000):
    grid_y = []
    for j in range(1000):
        grid_y.append(0)
    grid.append(grid_y)

# count overlapping points
points = 0

# filter lines
wanted_lines = []

# read lines
for line in content_list:
    duples = line.split(" -> ")
    x1y1 = duples[0].split(',')
    x2y2 = duples[1].split(',')
    if x1y1[0] == x2y2[0] or x1y1[1] == x2y2[1]:  # if x's or y's match
        wanted_lines.append([x1y1, x2y2])
        # only look at horizontal and vertical lines

# print(len(wanted_lines))  # this is correct on the sample

# iterate over grid
for i in range(0, len(wanted_lines)):
    x1 = int(wanted_lines[i][0][0])
    x2 = int(wanted_lines[i][1][0])
    y1 = int(wanted_lines[i][0][1])
    y2 = int(wanted_lines[i][1][1])
    if x1 == x2:
        # check to go up or down
        if y2 >= y1:
            for space in range(int(y1), int(y2) + 1):  # up to and including
                grid[space][x1] += 1
                # print(x1, space, sample_grid[space][x1])
        elif y1 > y2:
            for space in range(int(y2), int(y1) + 1):
                grid[space][x1] += 1
                # print(x1, space, sample_grid[space][x1])
    elif y1 == y2:
        # check to go left or right
        if x2 >= x1:
            for space in range(int(x1), int(x2) + 1):
                grid[y1][space] += 1
                # print(space, y1, sample_grid[y1][space])
        elif x1 > x2:
            for space in range(int(x2), int(x1) + 1):
                grid[y1][space] += 1
                # print(space, y1, sample_grid[y1][space])
    # total iterations: 330

for i in range(1000):
    for j in range(1000):
        if grid[i][j] > 1:
            points += 1
print(points)
