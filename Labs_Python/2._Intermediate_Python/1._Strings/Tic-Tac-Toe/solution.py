import math

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
turn = 0

def printBoard(board):
    for i in range(0, len(board)):
        string = ""
        for j in range(0, len(board[i])):
            item = " "
            if board[i][j] == 1:
                item = "X"
            elif board[i][j] == 2:
                item = "O"
            string += " " + item + " "
            if j < (len(board[i]) - 1):
                string += "|"
        string += "       "
        for j in range(0, len(board[i])):
            string += " " + str(j + (i * 3) + 1) + " "
            if j < (len(board[i]) - 1):
                string += "|"
        print(string)
        string = ""
        if i < (len(board) - 1):
            print("-----------       -----------")

def resetBoard(board):
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            board[i][j] = 0
    return board

def checkWin(board):
    for i in range(0, 3):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != 0:
            return board[i][0]
        if board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] != 0:
            return board[0][i]
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] != 0:
        return board[0][2]
    return 0

def checkTie(board):
    for row in board:
        for block in row:
            if block == 0:
                return False
    return True


print("Welcome to Tic-Tac-Toe.")
print("")
while True:
    while True:
        player = "O"
        if turn == 0:
            player = "X"
        print(" -------It's " + player + "'s turn-------")
        printBoard(board)

        while True:
            userInput = int(input("Choose a place to move: "))
            row = math.floor((userInput - 1) / 3)
            col = (userInput - 1) % 3

            if userInput > 9 or userInput < 1:
                print("Invalid Slot.")
            elif board[row][col] != 0:
                print("You can't move there.")
            else: 
                board[row][col] = (turn + 1)
                break
        print("")
        print("")
        winner = checkWin(board)
        if winner != 0:
            print(player, "wins the game!")
            printBoard(board)
            print("")
            break
        elif checkTie(board):
            print("Tie Game!")
            print("")
            break

        if turn == 1:
            turn = 0
        else:
            turn = 1
    userInput = input("Play Again? (y/n): ")
    if userInput == "n":
        break 
    else: 
        board = resetBoard(board)
        print("")
        print("")
