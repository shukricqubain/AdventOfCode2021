def binary_analyze(report):
    # report = [
    #    "00100",
    #    "11110",
    #    "10110",
    #    "10111",
    #    "10101",
    #    "01111",
    #    "00111",
    #    "11100",
    #    "10000",
    #    "11001",
    #    "00010",
    #    "01010"
    # ]
    zero_count = [0] * 12
    one_count = [0] * 12
    most_common = [0] * 12
    least_common = [0] * 12
    for x in report:
        for y in range(12):
            if int(x[y]) == 0:
                zero_count[y] += 1
            else:
                one_count[y] += 1

    for x in range(12):
        if zero_count[x] > one_count[x]:
            most_common[x] = 0
            least_common[x] = 1
        else:
            most_common[x] = 1
            least_common[x] = 0

    gamma_rate = ''.join(str(e) for e in most_common)
    epsilon_rate = ''.join(str(e) for e in least_common)
    print(f'Gamma Rate: {gamma_rate}')
    print(f'Epsilon Rate: {epsilon_rate}')
    gamma_rate = '0b' + gamma_rate
    epsilon_rate = '0b' + epsilon_rate
    gamma = int(gamma_rate, 2)
    epsilon = int(epsilon_rate, 2)
    print(f'Gamma Rate: {gamma}')
    print(f'Epsilon Rate: {epsilon}')
    power = gamma * epsilon
    print(f'Power Consumption: {power}')


if __name__ == '__main__':
    # binary_analyze()
    binary_report = []
    with open("input.txt") as file:
        while line := file.readline().rstrip():
            binary_report.append(line)
    binary_analyze(binary_report)
