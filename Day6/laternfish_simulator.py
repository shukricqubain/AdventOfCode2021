# Simulates the breeding of laternfish over
# x number of days
def fish_simulator(fish_list, days):
    # fish_list.sort()
    for day in range(days):
        for index in range(len(fish_list)):
            if fish_list[index] == 0:
                fish_list[index] = 6
                fish_list.append(8)
            else:
                fish_list[index] -= 1
    print(len(fish_list))


# This method opens the input file
# Reads each line, and adds it to the fish string
# The string is then split by commas
# Then iterated over to add each individual number representing a fish
# To a list and then passed into a fish simulator method
if __name__ == '__main__':
    fish = ''
    list_fish = []
    with open("input.txt") as file:
        while line := file.readline().rstrip():
            fish += line
    fish = fish.split(',')
    for element in fish:
        list_fish.append(int(element))
    fish_simulator(list_fish, 80)
