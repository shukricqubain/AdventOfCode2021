# Counts the bits in the specified column
# Checks the most common bit and returns 1 or 0
def count_bit(report, column_bit, life_support):
    one = 0
    zero = 0
    # print(f'Column: {column_bit}')
    # count bits in column
    for x in report:
        if int(x[column_bit]) == 0:
            zero += 1
        else:
            one += 1

    # print results
    # print(f'Zero Count: {zero}')
    # print(f'One Count: {one}')

    # check the most common bit
    if one > zero and life_support == 'oxygen':
        return 1
    elif one > zero and life_support == 'c02':
        return 0
    elif zero > one and life_support == 'oxygen':
        return 0
    elif zero > one and life_support == 'c02':
        return 1
    elif one == zero and life_support == 'oxygen':
        return 1
    else:
        return 0


# based on the most or least common bit
# the report is updated
# returns updated list
def update_list(report, column_bit, common_bit):
    # print(f'Column: {column_bit}')
    # print(len(report))
    # print(report)
    updated_report = report.copy()
    if common_bit == 1:
        for x in report:
            if x[column_bit] == '0':
                updated_report.remove(x)
    else:
        for x in report:
            if x[column_bit] == '1':
                updated_report.remove(x)

    # set report equal to updated list
    report = updated_report
    # print(len(report))
    # print(report)
    return report


def binary_analyze(report):
    # report = [
    #    '00100',
    #    '11110',
    #    '10110',
    #    '10111',
    #    '10101',
    #    '01111',
    #    '00111',
    #    '11100',
    #    '10000',
    #    '11001',
    #    '00010',
    #    '01010',
    # ]
    report_oxygen = report.copy()
    report_c02 = report.copy()
    char_length = 12
    # check oxygen value
    for x in range(char_length):
        # count bits in column
        if len(report_oxygen) == 1:
            break
        common_bit = count_bit(report_oxygen, x, 'oxygen')
        # print(f'Most Common: {common_bit}')
        report_oxygen = update_list(report_oxygen, x, common_bit)

    # check c02 value
    for x in range(char_length):
        # count bits in column
        if len(report_c02) == 1:
            break
        common_bit = count_bit(report_c02, x, 'c02')
        # print(f'Least Common: {common_bit}')
        report_c02 = update_list(report_c02, x, common_bit)

    # print oxygen value
    oxygen = report_oxygen[0]
    oxygen = int(oxygen, 2)
    print(f'Oxygen Value: {oxygen}')
    # print c02 value
    c02 = report_c02[0]
    c02 = int(c02, 2)
    print(f'C02 Value: {c02}')
    print(f'Result: {oxygen * c02}')


# Opens file and loads each line into
# an array that is then passed to the binary analyzer method
if __name__ == '__main__':
    # binary_analyze()
    binary_report = []
    with open("input.txt") as file:
        while line := file.readline().rstrip():
            binary_report.append(line)
    binary_analyze(binary_report)
