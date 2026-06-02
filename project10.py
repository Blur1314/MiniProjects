#To add completed and total tasks and find percentage


tasks=[]

def enter():
    try:
        ttask = int(input("Enter total tasks: "))
        ctask = int(input("Enter completed tasks: "))
    except:
        print("Invalid Input")
        return

    percentage = (ctask / ttask) * 100
    percentage = int(percentage)
    percentage = str(percentage)

    lst = [ttask, ctask, percentage]
    tasks.append(lst)

def view():
    for i in tasks:
        print("Total tasks:" , i[0] , ", Completed task:", i[1],", Percentage:", i[2] ,"%")

while True:
    choi = input("What to do?(View/Add)").lower()
    if choi == "view":
        if tasks != []:

            view()
        else:
            print("No tasks available to view")
    elif choi == "add":
        enter()
    else:
        print("Invalid input")
