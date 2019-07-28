class Task:
    def __init__(self, title, description, completion=False):
        self.title = title
        self.description = description
        self.completion = completion

    def __repr__(self):
        string = "Not Done"
        if self.completion:
            string = "Done"
        return self.title + " | " + self.description + " | " + string

    def markDone(self):
        self.completion = True

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


todolist = []
todolist = loadList()

print("Welcome to my To-Do-List Application.")
while True:
    userCommand = input("What would you like to do? (add, list, finish [index], save, exit): ")

    if userCommand == "add":
        print("")
        print("Adding a new Item to the List...")
        title = input("What is the title of your item: ")
        description = input("What is the description of your item: ")
        newTask = Task(title, description)
        print("")
        print("New Task Created:")
        print(newTask)
        todolist.append(newTask)
        
    elif userCommand == "list":
        print("")
        print("Your To-Do-List:")
        index = 1
        for task in todolist:
            print(str(index) + ".", task)
            index += 1

    elif userCommand[0:6] == "finish":
        index = int(userCommand[7:(len(userCommand))])
        todolist[index - 1].markDone()
        print("Task marked as complete")
        print(todolist[index-1])

    elif userCommand == "save":
        saveList(todolist)
        print("Your list has been saved.")

    elif userCommand == "exit":
        print("Goodbye!")
        break
    else: 
        print("Command not recognized...")
    print("")
