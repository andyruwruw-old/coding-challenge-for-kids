# To Do List Hints

[Go Back to Lab Description](./README.md)

## 1.  `Finish` Parsing

When the user asks to finish a task, they give you an index as well. Identifying the command and parsing out the index can be done with substrings.

```
elif userCommand[0:6] == "finish":
    index = int(userCommand[7:(len(userCommand))])
```

No matter how many digits the index might be, this will be able to handle it.

## 2.  Save n' Load Functions

Heres samples of how to save and load the users tasks:

```
def saveList(todolist):
    outFile = open("text.txt", "w")
    for task in todolist:
        outFile.write(task.title)
        outFile.write("\n")
        outFile.write(task.description)
        outFile.write("\n")
        if task.completion:
            outFile.write("T")
        else:
            outFile.write("F")
        outFile.write("\n")
    outFile.close()
```

```
def loadList():
    todolist = []
    inFile = open("text.txt", "r")
    tracker = 0
    title = ""
    description = ""
    completion = False
    for line in inFile:
        if tracker == 0:
            title = line[:-1]
        elif tracker == 1:
            description = line[:-1]
        elif tracker == 2:
            if line[0] == "T":
                completion = True
            else:
                completion = False
            newTask = Task(title, description, completion)
            todolist.append(newTask)
        tracker = (tracker + 1) % 3
    return todolist
```

## 3. Deletion

Deletion from an array comes in a few different flavors. Which you choose to use depends on how you plan to use them.

- `remove` : Removes the first matching value, not index.
- `del` : Removes an item at a specific index.
- `pop` : Removes an item at a specific index and returns it.

Once you have an index, run either `del` or `pop` to remove it.

```
del todolist[index]
```

To remove all of the completed items, create a for loop that will delete any items marked as complete.

Sometimes its best to run backwards through the array to prevent indexes being messed up while you're looping through because of deletion.

## 4. User Files

The file opening function takes the file name as a parameter. Have users give a name, and concatenate that with `".text"`.

Pass that new value to an `open` function with the `"w"` (write) mode, and it will create a new file.

When the program is opened, prompt them for a user name and load the cooresponding `.txt` file.

```
userName = input("Username: ")
outFile = open(userName, "w")
```

[Go Back to Lab Description](./README.md)