for i in range(1, 100):

    multipleThree = (i % 3 == 0)
    multipleFive = (i % 5 == 0)

    if multipleFive and multipleThree:
        print("FizzBuzz")

    elif multipleThree:
        print("Fizz")

    elif multipleFive:
        print("Buzz")
        
    else:
        print(i)