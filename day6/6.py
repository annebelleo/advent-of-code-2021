# import itertools
content_list = open("day6.txt", "r").read()
# part 1 and 2
fish_list = [int(fish) for fish in content_list if fish.isdigit()]

fish_inv = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
for key in fish_inv:
    fish_inv[key] = fish_list.count(key)

for day in range(256):
    day_inv = fish_inv.copy()

    for key in day_inv:
        if key != 0:
            fish_inv[key-1] = day_inv[key]

    for fish in day_inv:
        if fish == 0:
            fish_inv[8] = day_inv[fish]
            fish_inv[6] += day_inv[fish]
    print(day)

print(day_inv)

sum = 0
for key in fish_inv:
    sum += fish_inv[key]
print(sum)
