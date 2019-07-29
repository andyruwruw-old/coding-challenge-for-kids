# Tic-Tac-Toe Print Function

[Go Back to Lab Description](./README.md)

```
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
            string += " " + str(j + (i * 3)) + " "
            if j < (len(board[i]) - 1):
                string += "|"
        print(string)
        string = ""
        if i < (len(board) - 1):
            print("-----------       -----------")
```