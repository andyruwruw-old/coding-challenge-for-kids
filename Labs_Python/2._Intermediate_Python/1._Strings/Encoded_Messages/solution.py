alph = []
enco = []
alphString = "abcdefghijklmnopqrstuvwxyz ."
for char in alphString:
    alph.append(char)
for char in alphString[::-1]:
    enco.append(char)
print("E N C O D E D -  M E S S A G E S")
while True:
    userCommand = input("Encode or Decode: ")
    userInput = input("Text: ")
    final = ""
    if userCommand.lower().startswith("e"):
        for char in userInput:
            index = alph.index(char)
            final += enco[index]
    elif userCommand.lower().startswith("d"):
        for char in userInput:
            index = enco.index(char)
            final += alph[index]
    else: 
        print("Invalid.")
        continue
    print(final)
    quitVal = input("Exit? (y/n): ")
    if quitVal.lower().startswith("y"):
        break
