
tasks= []

def addtask():
    taskname = input("Enter task name: ")
    taskpriority =input("Enter task priority(High/Medium/Low): ").lower()
    if taskpriority == "high":
        currtask= [taskname,taskpriority]
        tasks.append(currtask)
        return currtask

def vieall():
    if tasks != []:
        for i in tasks:
            print("\nHigh priority tasks: ")
            print("Task name:",i[0], ", Task priority:",i[1],"\n")
    else:
        print("No High priority tasks! ")


while True:
    choice = input("Enter your choice(Add task/View task)").lower()
    if choice == "add task":
        addtask()
    elif choice == "view task":
        vieall()

    else:
        print("Invalid choice")
