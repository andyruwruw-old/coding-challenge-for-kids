// Problem 1: The Staircase

void theStaircase(int num)
{
    for (unsigned int i = 1; i < num + 1; i++)
    {
        for (unsigned int j = 1; j < i + 1; j++)
        {
            cout << j << " ";
        }
        cout << endl;
    }
}

// Problem 2: Flip-It

void flipIt(int num)
{
    for (unsigned int i = 0; i < num + 1; i++)
    {
        for (unsigned int j = 1; j < num + 1 - i; j++)
        {
            cout << j << " ";
        }
        cout << endl;
    }
}

// Problem 3: Backwards Now

def backwardsNow(num):
    for (unsigned int i = 0; i < (1, num + 1):
        string = ""
        for j in range(0, i):
            string += str(num - j) + " "
        print(string) 

// Problem 4: Flip-It Backwards

def flipItBackwards(num):
    for (unsigned int i = 0; i < (1, num + 1):
        string = ""
        for j in range(0, (num - i + 1)):
            string += str(num - j) + " "
        print(string) 

// Problem 5: Sharp Bump

def sharpBump(num):
    for (unsigned int i = 0; i < (0, num + 1):
        string = ""
        for j in range(1, i + 1):
            string += str(j) + " "
        print(string) 
    for (unsigned int i = 0; i < (0, num):
        string = ""
        for j in range(1, (num - i)):
            string += str(j) + " "
        print(string)

// Problem 6: Pointy Corner

def pointyCorner(num):
    for (unsigned int i = 0; i < (0, num):
        string = ""
        for j in range(1, (num + 1 - i)):
            string += str(j) + " "
        print(string)
    for (unsigned int i = 0; i < (2, num + 1):
        string = ""
        for j in range(1, i + 1):
            string += str(j) + " "
        print(string) 

// Problem 7: If and Then

def ifAndThen(num):
    for (unsigned int i = 0; i < (0, num):
        string = ""
        for j in range(0, num):
            if i == j:
                string += str(j)
            else:
                string += "0"
        print(string)

// Problem 8: Binary Staircase

def binaryStaircase(num):
    for (unsigned int i = 0; i < (0, num + 1):
        string = ""
        switch = True
        for j in range(1, i + 1):
            if switch:
                string += "1"
            else:
                string += "0"
            switch = not switch
        print(string)
            

// Problem 9: Binary Block

def binaryBlock(num):
    switch = True
    for (unsigned int i = 0; i < (0, num + 1):
        string = ""
        for j in range(0, num):
            if switch:
                string += "1"
            else:
                string += "0"
            switch = not switch
        print(string)

// Problem 10: Strange Layers

def strangeLayers(num):
    for (unsigned int i = 0; i < (0, num):
        string = ""
        for j in range(0, num):
            if (num - j <= i + 1):
                string += str(i + 1)
            else:
                string += "1"
        print(string)

// Problem 11: Palindromes

def palindromes(num):
    for (unsigned int i = 0; i < (0, num + 2):
        string = ""
        toggle = 1
        for j in range(1, i):
            string += str(j) + " "
        for j in range(i - 2, 0, -1):
            string += str(j) + " "
        print(string)

// Problem 12: Hanging by a Thread

def hangingByAThread(num):
    for (unsigned int i = 0; i < (0, num):
        string = ""
        for j in range(1, num + 1):
            if (j > i):
                string += str(j)
            else:
                string += " "
        print(string)
    for (unsigned int i = 0; i < (2, num + 1):
        string = ""
        for j in range(1, num + 1):
            if (j > num - i):
                string += str(j)
            else:
                string += " "
        print(string)


// Problem 13: Vertical Counting

def verticalCounting(num):
    for (unsigned int i = 0; i < (1, num + 1):
        string = ""
        for j in range(0, i):
            addnum = 0
            colnum = num
            for k in range(0, j):
                addnum += colnum
                colnum -= 1
            printnum = (i - j) + addnum
            string += str(printnum)
            string += " "
        print(string)


// Problem 14: Even Diamond

import math

def evenDiamond(num):
    //// Requires Odd Number
    if (num % 2 == 0): 
        return 0
    numbers = 1
    rate = 2
    mid = math.ceil(num / 2)
    for (unsigned int i = 0; i < (0, num):
        string = ""
        for j in range(0, num - numbers):
            string += " "
        for j in range(0, numbers):
            string += str(j + 1)
            string += " "
        print(string)
        if i == mid - 1:
            rate = -rate
        numbers += rate

// Problem 15: Even Hourglass

import math

def evenHourglass(num):
    //// Requires Odd Number
    if (num % 2 == 0): 
        return 0
    numbers = num
    rate = -2
    mid = math.ceil(num / 2)
    for (unsigned int i = 0; i < (0, num):
        string = ""
        for j in range(0, num - numbers):
            string += " "
        for j in range(0, numbers):
            string += str(j + 1)
            string += " "
        print(string)
        if i == mid - 1:
            rate = -rate
        numbers += rate

// Problem 16: Offset Diamond

import math

def offsetDiamond(num):
    numbers = 1
    rate = 1
    mid = num - 1
    for (unsigned int i = 0; i < (0, num * 2 - 1):
        string = ""
        for j in range(0, num - numbers):
            string += " "
        for j in range(0, numbers):
            string += str(j + 1)
            string += " "
        print(string)
        if i == mid:
            rate = -rate
        numbers += rate

// Problem 17: Offset Hourglass
import math

def offsetHourglass(num):
    numbers = num
    rate = -1
    mid = num - 1
    for (unsigned int i = 0; i < (0, num * 2 - 1):
        string = ""
        for j in range(0, num - numbers):
            string += " "
        for j in range(0, numbers):
            string += str(j + 1)
            string += " "
        print(string)
        if i == mid:
            rate = -rate
        numbers += rate


