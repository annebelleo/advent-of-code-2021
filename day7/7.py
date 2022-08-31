content_list = open("day7.txt", "r").read().splitlines()
content_list = content_list[0].split(',')
content_list = [int(x) for x in content_list]

# part 1 and 2
place = max(content_list)
initial_sum = 1000000000
for i in range(0, place):
    sum = 0
    for i in content_list:
        sum += (abs(place-i)) * (abs(place-i) + 1) // 2
    place -= 1
    if sum < initial_sum:
        initial_sum = sum
    sum = 0
print(initial_sum)
