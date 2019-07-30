# Bagels

Implement the guessing game of Bagels!

---

## 1. Details

Bagels is a simple game you can play with a friend. Your friend thinks up a random 3-digit number with no repeating digits, and you try to guess what the number is.

After each guess, your friend gives you clues on how close your guess was. 

If the friend tells you `bagels`, that means that none of the three digits you guessed was in the secret number.

If your friend tells you `pico`, then one of the digits is in the secret number, but your guess has the digit in the wrong place.

If your friend tells you `fermi`, then your guess has a correct digit in the right place.

Of course, even if you get a `pico` or `fermi` clue, you still don't know which digit in your guess is the correct one.

You can also get multiple clues after each guess. Say the secret number is `456`, and your guess is `546`. The clue you get from your friend would be `fermi pico pico` because one digit is correct and in the correct place (digit 6), and two digits are in the secret number but in the wrong place (digits 4 and 6).

Uses: Loops, If Statements, String, Functions, Random

---

## 2. Sample Output

```

I am thinking of a 3-digit number. Try guessing what it is.
Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.
I have thought of a number. You have 10 guesses to get it.
Guess #1:
123
Fermi
Guess #2:
456
Pico
Guess #3:
425
Fermi
Guess #3:
326
Bagels
Guess #3:
489
Bagels
Guess #3:
075
Fermi Fermi
Guess #3:
015
Fermi Pico
Guess #3:
175
You got it!
Do you want to play again? (yes or no)
no
```

---

## 3. Solution Links
[Solution](./solution.py)
