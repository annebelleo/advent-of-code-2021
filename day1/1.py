# part 1
content_list = open("day1.txt", "r").readlines()
integer_map = map(int, content_list)
integer_list = list(integer_map)
no_increases = 0
for i in range(1, len(integer_list)):
    if integer_list[i-1] < integer_list[i]:
        no_increases += 1
print(no_increases)
# part 2
no_increases = 0
for i in range(0, len(integer_list)-3):
    if integer_list[i] + integer_list[i+1] + integer_list[i+2] < integer_list[i+1] + integer_list[i+2] + integer_list[i+3]:
        no_increases += 1
print(no_increases)
