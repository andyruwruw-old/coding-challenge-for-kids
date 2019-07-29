# Sonar Treasure Hunt Print Functions

## Getting Row from Board as String
```
def getRow(board, row):
    boardRow = ''
    for i in range(60):
        boardRow += board[i][row]
    return boardRow
```
## Printing Generating New Board
```
def getNewBoard():
    board = []
    for x in range(60):
        board.append([])
        for y in range(15):
            if random.randint(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')
    return board
```
## Printing Board
```
def drawBoard(board):
    hline = '  '
    for i in range(1, 6):
        hline += (' ' * 9) + str(i)
    print(hline)
    print('  ' + ('0123456789' * 6))
    print()
    for i in range(15):
        if i < 10:
            extraSpace = ' '
        else:
            extraSpace = ''
        print('%s%s %s %s' % (extraSpace, i, getRow(board, i), i))
    print()
    print('  ' + ('0123456789' * 6))
    print(hline)
```
## Printing Instructions
```
def showInstructions():
    print('''Instructions: 
You are the captain of the Simon, a treasure-hunting ship. Your current mission
is to find the three sunken treasure chets that are lurking in the part of the 
ocen you are in and collect them.

To play, enter the coordinates of the point in the ocean you wish to drop a 
sonar device. The sonar can find out how far away the closest chest is to it.
For example, the d below marks where the device was dropped, and teh 2's
represent distances of 2 away from the device. The 4's represent
distances of 4 away from the device.

    444444444
    4       4
    4 22222 4
    4 2   2 4
    4 2 d 2 4
    4 2   2 4 
    4 22222 4
    4       4
    444444444

Press enter to continue...''')
    input()
    print('''For example, here is a treasure chest (the c) located a distance of 2 away
from the sonar device (the d):

      22222
      c   2
      2 d 2
      2   2
      22222

The point where the device was dropped will be marked with a 2.

The treasure chests don't move around. Sonar devices can detect treasure
chests up to a distance of 9. If all chests are out of range, the point
will be marked with O

If a device is directly dropped on a treasure chest, you ahve discovered
the location of the chest, and it will be collected. The sonar device will
remain there.

When you collect a chest, all sonar devices will update to locate the next
closest sunken treasure chest.

Press enter to continue...''')
    input()
    print()
```