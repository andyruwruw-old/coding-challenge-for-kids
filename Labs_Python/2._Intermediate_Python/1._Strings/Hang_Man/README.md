# Hang Man

Implement the game of hangman!

---

## 1. Details

Create a list with each of the letters of your desired word. Try to use a for loop to insert the letters from a string instead of hard coding it.
```
secretWord = ['p', 'i', 'n', 'e', 'a', 'p', 'p', 'l', 'e']
```

Ask the player their letter guess. Tell them whether it's wrong or not!

After each turn, print out all their wrong guesses.
```
Wrong: a, d, e, f
```
And then print out the word with all unguessed letters as underscores.
```
_ o _ t h
```

Make sure their selections work with both upper and lowercase letters.

Keep track of their wrong guesses and tell them if they lose after 8 wrong!

Don't let them repeat guesses and don't mark them wrong if they guess something they've already guessed!

---

## 2. Sample Output

```
Welcome to Hangman!

You have 8 lives remaining to guess the word.
_ _ _ _ _ _ _ _ _
Wrong:

Guess a letter: b
Wrong!

You have 7 lives remaining to guess the word.
_ _ _ _ _ _ _ _ _
Wrong: b

Guess a letter: a
Right!

You have 7 lives remaining to guess the word.
_ _ _ _ a _ _ _ _
Wrong: b

Guess a letter: e
Right!

You have 7 lives remaining to guess the word.
_ _ _ e a _ _ _ e
Wrong: b

Guess a letter: p
Right!

You have 7 lives remaining to guess the word.
p _ _ e a p p _ e
Wrong: b

Guess a letter: i
Right!

You have 7 lives remaining to guess the word.
p i _ e a p p _ e
Wrong: b

Guess a letter: b
You already guessed that!

Guess a letter: p
You already guessed that!

Guess a letter: n
Right!

You have 7 lives remaining to guess the word.
p i n e a p p _ e
Wrong: b

Guess a letter: l
Right!

Congrats you guess the word with 7 lives remaining!
p i n e a p p l e
Wrong: b
```

---
## 3. Futher Challenges

Try to take the secret word as a user input to keep things interesting!

You should print enough lines after input is taken in so the next player can't see what they put!

Allow the use of spaces, and print those automatically, they shouldn't count as a guess.

Variable:
```
secretWord = ['a', ' ', 'f', 'u', 'l', 'l', '', 's', 'e', 'n', 't', 'e', 'n', 'c', 'e', ]
```
Output:
```
_   _ _ _ _   _ _ _ _ _ _ _ _
```
---

## 4. Solution Links

[Need a Hint](./HINT.md)

[Solution](./solution.py)