badWord = input("What word would you like removed: ").lower()
sentence = input("What is the string for censorship: ")

wordList = sentence.split()

newString = ""
for word in wordList:
    if word.lower() == badWord:
        for char in word:
            newString += "*"
    else:
        newString += word
    newString += " "

print(newString)
