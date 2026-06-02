employee = []


def takeinput():
    employees = input("Enter employee name: ")
    taskno = int(input("Enter enter no of tasks: "))
    if taskno > 4:
        overload = True
    else:
        overload = False
    lst = [employees, taskno, overload]
    employee.append(lst)
    return lst
def getemp():
    name = input("Enter Employee name: ")
    for i in employee:
        if i[0] == name:
            return i


def checkoverload(para):
    try:
        if para[2] == True:
            print("Overloaded employee")

        elif para[2] == False:
            print("Not Overloaded employee")
    except:
        print("No such employee")

def view():
    for i in employee:
        print("Employee name: ",i[0],", Number of tasks:",i[1],", Overloaded?",i[2])

while True:
    choice = input("Enter your choice(View/Check Overload/Add employee): ").lower()
    if choice == "view":
        if employee != []:
            print(employee)
            view()
        else:
            print("No Employee added yet!")


    elif choice == "check overload":
        if employee != []:
            emploe = getemp()
            checkoverload(emploe)
        else:
            print("No record added yet!")
    elif choice == "add employee":

        takeinput()


    else:
        print("Invalid choice!")