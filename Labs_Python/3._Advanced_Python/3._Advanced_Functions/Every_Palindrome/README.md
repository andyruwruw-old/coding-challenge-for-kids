# Every Palindrome

Given a string, find every palindrome in the string.

---

## 1. Details

You need to sort through `every possible substring` of the given `string` and check if it's a palindrome.

The easiest way to implement this is with `recursion`. Recursion is the act of a fuction calling itself.

Recursion needs two things to work properly.
1. Call itself.
2. End cases.

For example in the following program:
```
def recursive(string, depth):
    if depth > 3:
        return True
    print(string)
    recursive(string + "1", depth + 1)
    recursive(string + "0", depth + 1)

recursive("", 0)
```
The `if statement` serves as our `end case`. Each time the function is called, depth is increased by one. If depth reaches a value of 4, no more function calls are made due to the `return True`, which will end that recursive path.

In the case of this lab, we first need a `function` that takes a string, and returns true or false if the string is a palindrome.

Our recursive formula should call itself twice, in a way that finds every possible substring.

--- 

## 3. Futher Challenges

Recursion can be timely and inefficient. In this case your program might be checking the same string multiple - if not many times! Add a feature to your code that will prevent the function from checking any substrings it has already checked.

---

## 3. Solution Links

[Hint](./HINT.md)

[Solution](./solution.py)