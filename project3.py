
father=[]
def initiatiation():
    empntask = {}
    prj ={}
    pname = input("Enter project name: ")
    no= int(input("Enter number of employees: "))
    for i in range(no):
        ename = input("Enter employee name: ")
        task = input("Enter task: ")
        empntask[ename] = task

    prj[pname] = empntask
    father.append(prj)


def viewall():
    for i in father:
        print("\n")
        for key , value in i.items():
            print("Project Name: ", key)
            for key , value in value.items():
                print("Employee Name: ", key ,",  Task: ", value)


while True:
    inp = input("INI / VIEW ALL ").upper()
    if inp == "INI":
        initiatiation()
    elif inp == "VIEW ALL":
        if father != []:
            print("\n")
            viewall()
            print("\n")
        else:
            print("No projects found")
            continue
    else:
        print("Invalid input")
        continue
    while True:
        cont = input("Continue? (Y/N) ").upper()
        if cont == "Y":
            break
        elif cont == "N":
            print("Exiting...")
            quit()
        else:
            print("Invalid input")
            continue






