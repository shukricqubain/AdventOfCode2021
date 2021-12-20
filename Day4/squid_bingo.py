import re


# This method takes the list of numbers representing an
# individual bingo board and checks the rows and columns for bingo.
# This is done by counting the bits in each individual row and column
# if the count equals 5 the board has bingo
# Returns a string with 'not winning' if the counts are below 5 or
# the row or column that has bingo
def calculate_bingo(board):
    # sum the rows
    rc_one = board[0] + board[1] + board[2] + board[3] + board[4]
    rc_two = board[5] + board[6] + board[7] + board[8] + board[9]
    rc_three = board[10] + board[11] + board[12] + board[13] + board[14]
    rc_four = board[15] + board[16] + board[17] + board[18] + board[19]
    rc_five = board[20] + board[21] + board[22] + board[23] + board[24]
    # sum the columns
    cc_one = board[0] + board[5] + board[10] + board[15] + board[20]
    cc_two = board[1] + board[6] + board[11] + board[16] + board[21]
    cc_three = board[2] + board[7] + board[12] + board[17] + board[22]
    cc_four = board[3] + board[8] + board[13] + board[18] + board[23]
    cc_five = board[4] + board[9] + board[14] + board[19] + board[24]
    # checks the row and column counts
    if rc_one == 5:
        # print('Row One')
        return 'Row One'
    if rc_two == 5:
        # print('Row Two')
        return 'Row Two'
    if rc_three == 5:
        # print('Row Three')
        return 'Row Three'
    if rc_four == 5:
        # print('Row Four')
        return 'Row Four'
    if rc_five == 5:
        # print('Row five')
        return 'Row Five'
    if cc_one == 5:
        # print('Column One')
        return 'Column One'
    if cc_two == 5:
        # print('Column Two')
        return 'Column Two'
    if cc_three == 5:
        # print('Column Three')
        return 'Column Three'
    if cc_four == 5:
        # print('Column Four')
        return 'Column Four'
    if cc_five == 5:
        # print('Column five')
        return 'Column Five'
    return 'not winning'


# Goes through the bingo numbers
# Checks if each board has the current bingo number,
# if it does, an empty board representing the current board is updated
# to a 1 instead of 0, marking the location of the number on the board
# once a board has five marks it stops checking and returns the
# winning number and board
def check_bingo(bingo_numbers, boards, empty_bingo_boards):

    # iterate over the bingo numbers
    for n in bingo_numbers:
        # iterate over the boards
        for b in range(len(boards)):
            try:
                index = boards[b].index(n)
            except ValueError:
                print(f'The number {n} is not in board {b + 1}')
                # set index to 26, so that we don't add a 1
                # even though the number isn't on the board
                index = 26
            if index < 25:
                empty_bingo_boards[b][index] = 1
            # check if the current board has bingo
            message = calculate_bingo(empty_bingo_boards[b])
            # print(f'Current Number: {n}, Current Board: {b + 1}, {message}')
            if message != 'not winning':
                return f'{n},{b}'


# uses the winning number, board, and corresponding zero board to calculate the score
# returns the score
def calculate_score(winning_bn, boards, zero_boards):
    winning_bn = winning_bn.split(',')
    winning_number = int(winning_bn[0])
    winning_board = int(winning_bn[1])
    total_score = 0
    for i in range(25):
        # add up all unmarked numbers
        if zero_boards[winning_board][i] == 0:
            total_score += boards[winning_board][i]
    total_score *= winning_number
    return total_score


# Checks for bingo among input boards and numbers
def squid_bingo(bingo_numbers, bingo_boards, zero_boards):
    winning_bn = check_bingo(bingo_numbers, bingo_boards, zero_boards)
    print(winning_bn)
    score = calculate_score(winning_bn, bingo_boards, zero_boards)
    print(score)


# Loads file
# Create list containing bingo numbers
# Create list of boards
# Creates list of empty boards as a way to keep track
# of bingo numbers on a board and to tell when a board has bingo
if __name__ == '__main__':
    string_numbers = ''
    numbers = []
    board_string = ''
    input_boards = []
    empty_boards = []
    # open file
    with open("input.txt") as file:
        # load bingo numbers into a list
        while line := file.readline().rstrip():
            string_numbers += line
        # split the numbers in the string to make loading
        # the numbers into the list easier
        string_numbers = string_numbers.split(',')
        for element in string_numbers:
            numbers.append(int(element))
        # load boards into a string
        count = 0
        # grab each row of numbers from the file
        # reformat the row to remove white space
        # add it to the board string
        for row in file:
            row = re.findall(r"[-+]?\d*\.\d+|\d+", row)
            row = ' '.join(row)
            board_string += row + ' '
            if count == 5:
                board_string += '\n'
                count = 0
            else:
                count += 1
        # split the board string by new line
        # to make adding each individual board to a list easier
        board_string = board_string.split('\n')
        current_board = []
        # add the boards into a list
        # add a list of 0s to the empty boards list
        for x in range(len(board_string)):
            current_board = list(map(int, board_string[x].split()))
            input_boards.append(current_board)
            empty_boards.append(list([0] * 25))
        # call the squid bingo method to calculate bingo
        squid_bingo(numbers, input_boards, empty_boards)
