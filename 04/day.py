def generalized(input_data):
    def win_number(board, numbers):
        def check_board(n):
            for i in range(len(board)):
                for j in range(len(board)):
                    if board[i][j] == n:
                        checked[i][j] = True
                        return

        def check_win():
            for r in checked:
                if all(r):
                    return True

            for c in [[r[i] for r in checked] for i in range(len(checked[0]))]:
                if all(c):
                    return True

            return False

        checked = [[False] * len(board) for _ in range(len(board))]
        for idx, i in enumerate(numbers):
            check_board(i)
            if check_win():
                missing = sum([board[i][j] for i in range(len(board)) for j in range(len(board)) if not checked[i][j]])
                return idx, i * missing

    numbers, boards = input_data
    return sorted([win_number(b, numbers) for b in boards])

def prep_data(inp):
    numbers = list(map(int, inp[0].strip().split(",")))
    data = []
    tmp = []
    for line in inp[2:]:
        l = line.strip()
        if not l:
            data.append(tmp)
            tmp = []
        else:
            tmp.append(list(map(int, l.replace("  ", " ").split(" "))))
    if len(tmp):
        data.append(tmp)

    return numbers, data

with open("input_test.txt") as f:
    data_test = prep_data(f.readlines())

with open("input.txt") as f:
    data = prep_data(f.readlines())

all_solutions = generalized(data_test)
assert all_solutions[0][1] == 4512
assert all_solutions[-1][1] == 1924

all_solutions = generalized(data)
print(all_solutions[0][1])
print(all_solutions[-1][1])