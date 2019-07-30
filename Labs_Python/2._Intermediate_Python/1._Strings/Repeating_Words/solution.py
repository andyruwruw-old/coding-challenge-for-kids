sentence = "" # Place the sentence here.

lastWord = ""
result = ""

for word in sentence.split():
    if word != lastWord:
        result += word + " "
        lastWord = word

print(result)
