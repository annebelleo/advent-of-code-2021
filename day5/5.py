# part 1 and part 2
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
        # look at horizontal and vertical lines
        wanted_lines.append([x1y1, x2y2])
        # part 2: look at diagonal lines
    elif abs(int(x1y1[0]) - int(x2y2[0])) == abs(int(x1y1[1]) - int(x2y2[1])):
        wanted_lines.append([x1y1, x2y2])


# iterate over grid
for i in range(len(wanted_lines)):
    x1 = int(wanted_lines[i][0][0])
    x2 = int(wanted_lines[i][1][0])
    y1 = int(wanted_lines[i][0][1])
    y2 = int(wanted_lines[i][1][1])
    if x1 == x2:
        for space in range(min(y1, y2), max(y1, y2) + 1):  # up to and including
            grid[space][x1] += 1
    elif y1 == y2:
        for space in range(min(x1, x2), max(x1, x2) + 1):
            grid[y1][space] += 1
    elif abs(x1 - x2) == abs(y1 - y2):  # all diagonals
        if x2 >= x1:
            for space in range(int(x1), int(x2) + 1):
                grid[y1][space] += 1
                if y2 >= y1:
                    y1 += 1
                else:
                    y1 -= 1
        elif x1 > x2:
            for space in range(int(x2), int(x1) + 1):
                grid[y2][space] += 1
                if y2 > y1:
                    y2 -= 1
                else:
                    y2 += 1

        # horizontal/vertical total iterations: 330
        # + diagonal iterations: 498

# iterate through grid to calculate number of points
for i in range(1000):
    for j in range(1000):
        if grid[i][j] > 1:
            points += 1
print(points)
