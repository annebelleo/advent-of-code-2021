content_list = open("day2.txt", "r").read().splitlines()
directions = []
for i in content_list:
    words = i.split(' ')
    directions.append(words)
print(directions)
