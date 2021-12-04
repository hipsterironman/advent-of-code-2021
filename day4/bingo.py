contents = []
with open('/Users/ryan/develop/advent-of-code-2021/day4/input.txt') as f:
    contents = f.read().split('\n')

MARKED = 1
UNMARKED = 0


def check_for_bingo(board):
    if any(all(row.values()) for row in board):
        return True

    for i in range(0, 5):
        if all(list(row.values())[i] for row in board):
            return True

    return False


def sum_for_bingo(board):
    return sum(sum(val for (val, marked) in row.items() if not marked) for row in board)


def play_bingo(instructions, boards):
    non_winning_boards = boards
    winning_boards = []

    for num in instructions:
        for board in non_winning_boards:
            for row in board:
                row[num] = MARKED if num in row else UNMARKED

            if check_for_bingo(board):
                winning_boards.append(board)
                if len(winning_boards) == len(boards):
                    return sum_for_bingo(board) * num

        non_winning_boards = [
            board for board in non_winning_boards if board not in winning_boards]


bingo_instructions = [int(num) for num in contents[0].split(',')]
bingo_boards = []
curr_board = []
bingo_board_input = contents[2:]

for line in bingo_board_input:
    if line == '':
        bingo_boards.append(curr_board)
        curr_board = []
    else:
        curr_board.append({}.fromkeys([int(num)
                          for num in line.split(' ') if num != ''], UNMARKED))


print(play_bingo(bingo_instructions, bingo_boards))
