string = "racecars are my favorite my dood"
pal = []
checked = []

def checkPal(string):
    for i in range(0, len(string)):
        if i >= len(string) - 1 - i:
            return True
        if string[i] != string[len(string) - 1 - i]:
            return False
    return True

def findAllPal(string):
    if string in checked:
        return True
    checked.append(string)
    print(string)
    if len(string) == 1:
        return True
    if checkPal(string):
        if string not in pal:
            pal.append(string)
    findAllPal(string[:-1])
    findAllPal(string[1:])



findAllPal(string)
print(pal)
print(checked)
