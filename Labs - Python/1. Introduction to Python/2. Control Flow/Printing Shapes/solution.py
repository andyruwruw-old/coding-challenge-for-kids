# Problem 1: The Staircase

def theStaircase(num):
    for i in range(0, num + 1):
        string = ""
        for j in range(1, i + 1):
            string += str(j) + " "
        print(string)   

# Problem 2: Flip-It

def flipIt(num):
    for i in range(0, num + 1):
        string = ""
        for j in range(1, (num + 1 - i)):
            string += str(j) + " "
        print(string) 

# Problem 3: Backwards Now

def backwardsNow(num):
    for i in range(1, num + 1):
        string = ""
        for j in range(0, i):
            string += str(num - j) + " "
        print(string) 

# Problem 4: Flip-It Backwards

def flipItBackwards(num):
    for i in range(1, num + 1):
        string = ""
        for j in range(0, (num - i + 1)):
            string += str(num - j) + " "
        print(string) 

# Problem 5: Sharp Bump

def sharpBump(num):
    for i in range(0, num + 1):
        string = ""
        for j in range(1, i + 1):
            string += str(j) + " "
        print(string) 
    for i in range(0, num):
        string = ""
        for j in range(1, (num - i)):
            string += str(j) + " "
        print(string)

# Problem 6: Pointy Corner

def pointyCorner(num):
    for i in range(0, num):
        string = ""
        for j in range(1, (num + 1 - i)):
            string += str(j) + " "
        print(string)
    for i in range(2, num + 1):
        string = ""
        for j in range(1, i + 1):
            string += str(j) + " "
        print(string) 

# Problem 7: If and Then

def ifAndThen(num):
    for i in range(0, num):
        string = ""
        for j in range(0, num):
            if i == j:
                string += str(j)
            else:
                string += "0"
        print(string)

# Problem 8: Binary Staircase

def binaryStaircase(num):
    for i in range(0, num + 1):
        string = ""
        switch = True
        for j in range(1, i + 1):
            if switch:
                string += "1"
            else:
                string += "0"
            switch = not switch
        print(string)
            

# Problem 9: Binary Block

def binaryBlock(num):
    switch = True
    for i in range(0, num + 1):
        string = ""
        for j in range(0, num):
            if switch:
                string += "1"
            else:
                string += "0"
            switch = not switch
        print(string)

# Problem 10: Strange Layers

def strangeLayers(num):
    for i in range(0, num):
        string = ""
        for j in range(0, num):
            if (num - j <= i + 1):
                string += str(i + 1)
            else:
                string += "1"
        print(string)

# Problem 11: Palindromes

def palindromes(num):
    for i in range(0, num + 2):
        string = ""
        toggle = 1
        for j in range(1, i):
            string += str(j) + " "
        for j in range(i - 2, 0, -1):
            string += str(j) + " "
        print(string)

# Problem 12: Hanging by a Thread

def hangingByAThread(num):
    for i in range(0, num):
        string = ""
        for j in range(1, num + 1):
            if (j > i):
                string += str(j)
            else:
                string += " "
        print(string)
    for i in range(2, num + 1):
        string = ""
        for j in range(1, num + 1):
            if (j > num - i):
                string += str(j)
            else:
                string += " "
        print(string)


# Problem 13: Vertical Counting

def verticalCounting(num):
    for i in range(0, num):
        string = ""
        for j in range(0, i):
            string += str(i + (num * j))
            string += " "
        print(string)


# Problem 14: Even Diamond

def evenDiamond(num):

# Problem 15: Even Hourglass

def evenHourglass(num):

# Problem 16: Offset Diamond

def offsetDiamond(num):

# Problem 17: Offset Hourglass

def offsetHourglass(num):
