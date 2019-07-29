# Tic-Tac-Toe

Implement the game of Tic-Tac-Toe!

---


## 1. Details

Use an array of arrays to hold the board data.

Before each turn, print the board in the following fashion:
```
 O |   | X         1 | 2 | 3   
-----------       -----------
   | O |           4 | 5 | 6   
-----------       -----------
   |   | X         7 | 8 | 9   
```
This print function is [prewritten](PRINT.md), or you can write it yourself!

Tell the player it's their turn and ask where they'd like to move.
```
Player 1 Move: 
```
Players input integer positions cooresponding with the map on the right.

Check for winners and end the game when someone makes 3 in a row!

Make sure you end the game if the board fills up, and don't let someone play where someone else has gone.

---
## 2. Sample Output

```
Welcome to Tic-Tac-Toe.

 -------It's X's turn-------
   |   |           1 | 2 | 3 
-----------       -----------
   |   |           4 | 5 | 6 
-----------       -----------
   |   |           7 | 8 | 9 
Choose a place to move: 1


 -------It's O's turn-------
 X |   |           1 | 2 | 3 
-----------       -----------
   |   |           4 | 5 | 6 
-----------       -----------
   |   |           7 | 8 | 9 
Choose a place to move: 3


 -------It's X's turn-------
 X |   | O         1 | 2 | 3 
-----------       -----------
   |   |           4 | 5 | 6 
-----------       -----------
   |   |           7 | 8 | 9 
Choose a place to move: 5


 -------It's O's turn-------
 X |   | O         1 | 2 | 3 
-----------       -----------
   | X |           4 | 5 | 6 
-----------       -----------
   |   |           7 | 8 | 9 
Choose a place to move: 5
You can't move there.
Choose a place to move: 7


 -------It's X's turn-------
 X |   | O         1 | 2 | 3 
-----------       -----------
   | X |           4 | 5 | 6 
-----------       -----------
 O |   |           7 | 8 | 9 
Choose a place to move: 9


X wins the game!
 X |   | O         1 | 2 | 3 
-----------       -----------
   | X |           4 | 5 | 6 
-----------       -----------
 O |   | X         7 | 8 | 9 

Play Again? (y/n): n
```
---

## 3. Further Challenge

If the player doesn't enter an integer, tell them it's wrong and ask them again! 

---
## 4. Solution Links

[Need a Hint](./HINT.md)

[Solution](./solution.py)
