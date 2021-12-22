# Takes the coordinates of hydrothermal vents
# Separates first and second coordinate
# adds each individual number from coordinates to list
def organize_coordinates(coordinates):
    organized_vents = []
    # take string, grab first and second coordinate
    # store the four numbers in one row of an array
    for i in range(len(coordinates)):
        row_vents = []
        coordinates[i] = coordinates[i].split('->')
        # trim the white space
        coordinates[i][0] = coordinates[i][0].strip()
        coordinates[i][1] = coordinates[i][1].strip()
        # split to get individual numbers
        coordinates[i][0] = coordinates[i][0].split(',')
        coordinates[i][1] = coordinates[i][1].split(',')
        # store each individual number in a list
        row_vents.append((int(coordinates[i][0][0])))
        row_vents.append((int(coordinates[i][0][1])))
        row_vents.append((int(coordinates[i][1][0])))
        row_vents.append((int(coordinates[i][1][1])))
        organized_vents.append(row_vents)
    return organized_vents


# iterate through the list of vents,
# look for highest value
# return value to use when building ocean map
def get_dimensions(vent_list):
    highest = 0
    for num in range(len(vent_list)):
        if vent_list[num][0] > highest:
            highest = vent_list[num][0]
        if vent_list[num][1] > highest:
            highest = vent_list[num][1]
        if vent_list[num][2] > highest:
            highest = vent_list[num][2]
        if vent_list[num][3] > highest:
            highest = vent_list[num][3]
    return highest


# update the ocean floor map based on the
# coordinates contained in the vents_location list
def update_map(current_map, vents_location):
    # iterate through each set of coordinates of vents
    for vent in range(len(vents_location)):
        x_one = vents_location[vent][0]
        y_one = vents_location[vent][1]
        x_two = vents_location[vent][2]
        y_two = vents_location[vent][3]
        # take result to help determine which direction
        # we need to loop later on as well as the orientation
        # of the vent
        x_result = x_two - x_one
        y_result = y_two - y_one
        # update horizontal vents
        if x_result > 0 and y_result == 0:
            # iterate through ocean map by the horizontal result of the two coordinates
            for distance in range(x_result + 1):
                # updates the map value
                initial_value = current_map[y_one][x_one + distance]
                if initial_value != 0:
                    current_map[y_one][x_one + distance] = initial_value + 1
                else:
                    current_map[y_one][x_one + distance] = 1
        # update horizontal vents in opposite direction
        elif x_result < 0 and y_result == 0:
            # iterate through ocean map by the horizontal result of the two coordinates
            for distance in range(abs(x_result) + 1):
                # updates the map values
                initial_value = current_map[y_one][x_one - distance]
                if initial_value != 0:
                    current_map[y_one][x_one - distance] = initial_value + 1
                else:
                    current_map[y_one][x_one - distance] = 1
        # update vertical vents
        elif x_result == 0 and y_result > 0:
            # iterate through ocean map by the vertical result of the two coordinates
            for distance in range(y_result + 1):
                # updates the map values
                initial_value = current_map[y_one + distance][x_one]
                if initial_value != 0:
                    current_map[y_one + distance][x_one] = initial_value + 1
                else:
                    current_map[y_one + distance][x_one] = 1
        # update vertical vents in opposite direction
        elif x_result == 0 and y_result < 0:
            # iterate through ocean map by the vertical result of the two coordinates
            for distance in range(abs(y_result) + 1):
                # updates the map values
                initial_value = current_map[y_one - distance][x_one]
                if initial_value != 0:
                    current_map[y_one - distance][x_one] = initial_value + 1
                else:
                    current_map[y_one - distance][x_one] = 1
        # update diagonal vent with both positive x and y values
        elif x_result > 0 and y_result > 0:
            for distance in range(abs(y_result) + 1):
                # updates the map values
                initial_value = current_map[y_one + distance][x_one + distance]
                if initial_value != 0:
                    current_map[y_one + distance][x_one + distance] = initial_value + 1
                else:
                    current_map[y_one + distance][x_one + distance] = 1
        # update diagonal vent with both negative x and y values
        elif x_result < 0 and y_result < 0:
            for distance in range(abs(y_result) + 1):
                # updates the map values
                initial_value = current_map[y_one - distance][x_one - distance]
                if initial_value != 0:
                    current_map[y_one - distance][x_one - distance] = initial_value + 1
                else:
                    current_map[y_one - distance][x_one - distance] = 1
        # update diagonal vent with negative x and positive y values
        elif x_result < 0 < y_result:
            for distance in range(abs(y_result) + 1):
                # updates the map values
                initial_value = current_map[y_one + distance][x_one - distance]
                if initial_value != 0:
                    current_map[y_one + distance][x_one - distance] = initial_value + 1
                else:
                    current_map[y_one + distance][x_one - distance] = 1
        # update diagonal vent with positive x and negative y values
        elif x_result > 0 > y_result:
            for distance in range(abs(y_result) + 1):
                # updates the map values
                initial_value = current_map[y_one - distance][x_one + distance]
                if initial_value != 0:
                    current_map[y_one - distance][x_one + distance] = initial_value + 1
                else:
                    current_map[y_one - distance][x_one + distance] = 1
    return current_map


# Check for overlaps in ocean floor map
# and returns the count
def calculate_overlaps(vent_map):
    count = 0
    for j in range(len(vent_map)):
        for k in range(len(vent_map)):
            if vent_map[j][k] >= 2:
                count += 1
    return count


# Method opens file
# Reads in the coordinates of hydrothermal vents on ocean floor
# Cleans up the coordinates and creates 2dimensional list
# to easily parse each individual number of a singular vent's coordinate
# Creates an empty 2dimensional list representing ocean floor
# updates it with the coordinates of the vents
# Calculates the overlaps and prints the results
if __name__ == '__main__':
    # stores the coordinates containing
    # the ranges of vents
    with open("input.txt") as file:
        lines = file.readlines()
    # get coordinates in 2d list of numbers
    vents = organize_coordinates(lines)
    # find the highest value to use when making ocean floor map
    high_value = get_dimensions(vents)
    # create empty ocean map
    ocean_map = []
    for x in range(high_value + 1):
        ocean_map.append(list([0] * (high_value + 1)))
    # update the map based on vent coordinates
    updated_map = update_map(ocean_map, vents)
    # for z in range(len(updated_map)):
    #    print(updated_map[z])
    # calculate the amount of vent overlaps
    overlap_count = calculate_overlaps(updated_map)
    print(overlap_count)
