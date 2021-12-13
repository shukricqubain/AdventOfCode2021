# Day 1 of Advent of Code

# takes in list of numbers
# checks if previous number is larger or smaller
# stores the number of numbers that are larger than previous
def number_inc_dec(nums):
    # nums = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    prev = 0
    one = 0
    two = 0
    three = 0
    previous_sum = 0
    current_sum = 0
    inc = 0
    for x in nums:
        if len(nums) <= prev + 2:
            break
        one = nums[prev]
        two = nums[prev + 1]
        three = nums[prev + 2]
        # print(f'{one} {two} {three}')
        current_sum = one + two + three
        if previous_sum == 0:
            print(f'{current_sum} (N/A - no previous sum)')
            previous_sum = current_sum
            prev += 1
        elif current_sum > previous_sum:
            print(f'{current_sum} (increased)')
            previous_sum = current_sum
            prev += 1
            inc += 1
        elif current_sum == previous_sum:
            print(f'{current_sum} (no change)')
            previous_sum = current_sum
            prev += 1
        else:
            print(f'{current_sum} (decreased)')
            previous_sum = current_sum
            prev += 1
    print(f'{inc}')
    return inc


if __name__ == '__main__':
    num_list = []
    with open("input.txt") as file:
        while line := file.readline().rstrip():
            current = int(line)
            num_list.append(current)

    increase = number_inc_dec(num_list)
    print(f'\n{increase}')
