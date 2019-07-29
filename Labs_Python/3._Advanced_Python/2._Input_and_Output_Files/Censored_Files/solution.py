inFile = open("input.txt", "r")
outFile = open("output.txt", "w")

badWords = []

while True:
    badWord = input("What word would you like removed (/done to move on): ").lower()
    if badWord == "/done":
        break
    badWords.append(badWord.lower())

for line in inFile:
    words = line.split()
    newLine = ""
    for word in words:
        if word.lower() in badWords:
            for char in word:
                newLine += "*"
        else:
            newLine += word
        newLine += " "
    newLine += "\n"
    outFile.write(newLine)
outFile.close()
print("New File Created.")


