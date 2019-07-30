wordList = [] # Place the word list here.

longestWord = ""

for word in wordList:
    if len(word) > len(longestWord):
        longestWord = word

print("The longest word is:", longestWord)