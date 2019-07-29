print("Welcome to the Fibonacci Sequence generator!")
numNumbers = int(input("How many digits would you like? "))

lastNum = 1
lastLastNum = 1
if numNumbers > 0:
    print(str(lastLastNum))
if numNumbers > 1:
    print(str(lastNum))

for i in range(2, numNumbers):
    currentNum = lastNum + lastLastNum
    print(str(currentNum))

    lastLastNum = lastNum
    lastNum = currentNum