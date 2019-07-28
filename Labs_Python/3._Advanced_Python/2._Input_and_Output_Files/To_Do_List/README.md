# To Do list

Have the students implement their own To-Do-List application that allows them to save objects and retrieve them later.

---

## 1. Details

Each task should be its own object, holding three different values set by the constructor, with completion defaulted to `false`.

- `Task Title` : String
- `Task Description` : String
- `Task Completion` : Boolean

The following methods should be implemented:

- `markDone(self)` : Sets `completion` to `true`
- `__repr__` : Prints the object in a format with all information.

These tasks will be held in an `array`.

When the program is run, it will implement a `while` loop prompting the user for a command. The following should be implemented:

- `add` : Takes user input to add a new item to the list, printing the new item after.
- `list` : Prints all the items from the list.
- `finish` [index] : Marks the item at a given index as completed.
- `save` : Saves the list to an output file.
- `exit` : closes the program

`Add` should ask for a `title` and `description` but default `completion` to false.

`List` should display an index for each item, as shown below.

`Finish` will coorespond to the `list` functions indexes and mark the selected item as complete.

`Save` is the most important, and should read through the array of tasks, outputing their information to a `.txt` file in a way that can be read by the program upon opening.

When the program is first run, before it prompts for a command, it should look to this `.txt` file and create tasks from the saved information.

Prewritten save and load functions can be found the [Need a Hint](./HINT.md) document.

---

## 2. Sample Output


```
Welcome to my To-Do-List Application.

What would you like to do? (add, list, finish [index], save, exit): add

Adding a new Item to the List...
What is the title of your item: Do Laundry
What is the description of your item: By Sunday
New Task Created:
Do Laundry | By Sunday | Not Done

What would you like to do? (add, list, finish [index], save, exit): list
Your To-Do-List:
1. Math Homework | Chpt 4.3 | Not Done
2. Do Laundry | By Sunday | Not Done

What would you like to do? (add, list, finish [index], save, exit): finish 1
Completing Task 1
1. Math Homework | Chpt 4.3 | Done

What would you like to do? (add, list, finish [index], save, exit): list
Your To-Do-List:
1. Math Homework | Chpt 4.3 | Done
2. Do Laundry | By Sunday | Not Done

What would you like to do? (add, list, finish [index], save, exit): save
Your list has been saved.

What would you like to do? (add, list, finish [index], save, exit): exit
Goodbye!
```

---

## 3. Further Challenges

1. Implement the following functions.

    - `delete [index]` : Deletes task at Index.
    - `delete all` : Deletes all `done` tasks.

2. Have the program save after every change made, as opposed to only when the user specifies `save`.

3. Have the user be able to save to different files, and load from different files, to allow multiple users to use the same application.

---

## 4. Solution Links
[Need a Hint](./HINT.md)

[Solution](./solution.py)