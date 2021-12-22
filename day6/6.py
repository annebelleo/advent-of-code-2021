# import itertools
content_list = open("day6.txt", "r").read()
# part 1 and 2
fish_list = [int(fish) for fish in content_list if fish.isdigit()]

i = 0
while i < 256:
    for fish in range(len(fish_list)):
        if fish_list[fish] == 0:
            fish_list[fish] = 6
            fish_list.append(8)
        else:
            fish_list[fish] -= 1
    i += 1
    print(i)
