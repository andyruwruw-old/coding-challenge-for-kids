# Encoded Messages Hint

[Go Back to Lab Description](./README.md)

I would strongly recommend creating `two lists`, one with `regular letters`, the second with their corresponding `encoded letters`.

```
regular = ["a", "b", "c"]
encoded = ["*", "#", "^"]
```

Now to set these up, going through each letter and placing it in a list is a pain.

Instead, write out the letters in a `string`, and use a `for-loop` to place them in the list.

```
regular = []
alphabet = "abcdefghijklmnopqrstuvwxyz"

for letter in alphabet:
    regular.append(letter)
```

Remember that `.append()` just means to add the element to the end of the list.

For the encoded list of letters, I just used the same process, but reversed the list using `[::-1]`.

```
for letter in alphabet[::-1]:
    encoded.append(letter)
```

This means both the lists are copies of each other, but reversed.

To encode the message, I took the user's string, and went character by character.  For each character, I used `.index()` to find it's position in the `regular` list.

(Don't forget to `.lower()` the letters to turn them into lowercase)

```
for letter in userInput: 
    index = regular.index(letter.lower())
```

I then used that index to find its counterpart in the `encoded list` and add it to my final string.

```
encodedMessage = ""

for letter in userInput: 
    index = regular.index(letter.lower())
    encodedMessage += encoded[index]
```

The process is reversed to decode messages.

[Go Back to Lab Description](./README.md)