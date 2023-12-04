def map(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def checkWin(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def checkDraw(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def playXO():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        map(board)
        row = int(input(f"Player {current_player}, enter row (0, 1, 2): "))
        col = int(input(f"Player {current_player}, enter col (0, 1, 2): "))

        if board[row][col] == " ":
            board[row][col] = current_player
            if checkWin(board, current_player):
                map(board)
                print(f"Player {current_player} win!")
                break
            elif checkDraw(board):
                map(board)
                print("Draw!")
                break
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("This cell is already occupied. try again.")

playXO()