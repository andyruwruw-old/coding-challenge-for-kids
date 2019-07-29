import math
inFile = open("input.txt", "r")
outFile = open("output.txt", "w")

def getSpace(desired, length):
    space = ""
    for i in range(0, (desired - length)):
        space += " "
    return space

charCount = 0
dictionary = {}
discluded = ["\n", " "]

print("Reading Input File.")
for line in inFile:
    for char in line:
        if char in discluded:
            continue 
        elif char.lower() in dictionary:
            dictionary[char.lower()] += 1
        else:
            dictionary[char.lower()] = 1
        charCount += 1

print("Recording Data")
outFile.write("---------- CHARACTER FREQUENCIES ----------- \n" + str(len(dictionary))+ " UNIQUE CHARACTERS | " + str(charCount) + " TOTAL CHARACTERS\n")
outFile.write("--------------------------------------------\n")
for char, num in sorted(dictionary.items(), key=lambda tup: tup[1])[::-1]:
    charNum = str(num)
    charFreq = str(round((num / charCount * 100), 2)) 
    outFile.write("  " + char + "   |   " + charNum + getSpace(6, len(charNum)) + " | " + getSpace(8, len(charFreq)) + charFreq + "%" + "\n")
outFile.write("--------------------------------------------\n")
outFile.write("DISCLUDED CHARACTERS: space, newline")  

outFile.close()
print("Process Complete.")
