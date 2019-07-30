alph = []
enco = []
alphString = "abcdefghijklmnopqrstuvwxyz .,/;\'[]=-0987654321`\\|<>?:\"+_)(*&^%$#@!~"
for char in alphString:
    alph.append(char)
for char in alphString[::-1]:
    enco.append(char)
print("E N C O D E D -  M E S S A G E S")
while True:
    userCommand = input("Encode or Decode: ")
    userInput = input("Text: ")
    final = ""
    message = ""
    if userCommand.lower().startswith("e"):
        message = "Encoded:"
        for char in userInput:
            index = alph.index(char.lower())
            final += enco[index]
    elif userCommand.lower().startswith("d"):
        message = "Decoded:"
        for char in userInput:
            index = enco.index(char.lower())
            final += alph[index]
    else: 
        print("Invalid.")
        continue
    print()
    print(message, final)
    print()
    quitVal = input("Exit? (y/n): ")
    if quitVal.lower().startswith("y"):
        break