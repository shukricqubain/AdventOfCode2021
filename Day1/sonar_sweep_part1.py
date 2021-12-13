# Day 1 of Advent of Code

# takes in list of numbers
# checks if previous number is larger or smaller
# stores the number of numbers that are larger than previous
def number_inc_dec(nums):
    prev = 0
    inc = 0
    for x in nums:
        if prev == 0:
            print(f'{x}  (N/A - no previous measurement)')
            prev = x
        elif x > prev:
            print(f'{x}  (increased)')
            inc += 1
            prev = x
        else:
            print(f'{x}  (decreased)')
            prev = x
    return inc

# Opens input file
# creates a list of numbers that will
# be checked by number_inc_dec method
# prints the output
if __name__ == '__main__':
    num_list = []
    with open("input.txt") as file:
        while line := file.readline().rstrip():
            current = int(line)
            num_list.append(current)

    increase = number_inc_dec(num_list)
    print(f'\n{increase}')
