def calc_position(position):
    #
    # forward X increases the horizontal position by X units.
    # down X increases the depth by X units.
    # up X decreases the depth by X units.
    # output horizontal 15 depth 10

    # position = [
    #    "forward 5",
    #    "down 5",
    #    "forward 8",
    #    "up 3",
    #    "down 8",
    #    "forward 2"
    # ]
    horizontal = 0
    depth = 0
    for x in position:
        current = x.split(" ")
        if current[0] == "forward":
            # print(f'{current[0]} {current[1]}')
            horizontal += int(current[1])
        elif current[0] == "down":
            # print(f'{current[0]} {current[1]}')
            depth += int(current[1])
        else:
            # print(f'{current[0]} {current[1]}')
            depth -= int(current[1])
    print(f'Horizontal {horizontal}, Depth {depth}')
    print(f'{horizontal * depth}')


if __name__ == '__main__':
    instruction_list = []
    with open("input.txt") as file:
        while line := file.readline().rstrip():
            instruction_list.append(line)

    calc_position(instruction_list)
# calc_position()
