requests = []

def applyLeave():
    name = input("Enter your name: ").lower()
    leavedays = input("Enter amount of leave days: ").lower()
    requests.append([name, leavedays])

def viewall():

    for i in requests:
        try:
            if i[2] == True:
                pass
        except:

            print("Name:", i[0], " Leave days: ", i[1])

def getrequest(name):
    for i in requests:
        if i[0] == name:
            return i
    print("No such name")
    return []

def getindex(name):
    for i in requests:
        if i[0] == name:
            return requests.index(i)
    print("No such name")
    return []
def decide(lis):
    global requests
    decision = input("Accept or reject: ").lower()
    if decision == "accept":
        lis.append("accepted")
        requests.remove(requests[getindex(name)])
        requests.append(lis)

    elif decision == "reject":
        lis.append("rejected")
        requests.remove(requests[getindex(name)])
        requests.append(lis)
    else:
        print("Wrong input")
    return lis


while True:
    role = input("Enter your role(Manager/Employee): ").lower()
    if role == "manager":
        inp = input("What to do?(view/decide)").lower()
        if inp == "view":
            if requests != []:
                viewall()
            else:
                print("No requests made yet")
                continue
        elif inp == "decide":
            if requests != []:
                name = input("Enter employee name: ").lower()

                chosenlist = getrequest(name)
                if chosenlist == []:
                    print("Enter a proper name")
                    continue
                updated = decide(chosenlist)

            else:
                print("No requests made yet")
                continue
    elif role == "employee":
        inp = input("What to do?(view/apply)").lower()
        if inp == "view":
            if requests != []:
                for i in requests:
                    print("Name:", i[0], " Leave days: ", i[1])
            else:
                print("No requests made yet")
                continue
            enter= input("Enter the name to see status:").lower()
            chosenlist = getrequest(enter)
            try:
                if chosenlist[2] == "accepted":
                    print("Request was accepted by manager")
                elif chosenlist[2] == "rejected":
                    print("Request was rejected by manager")

                else:
                    pass
            except IndexError:
                if chosenlist != []:
                    print("Request was not evaluated by manager")

        elif inp == "apply":
            applyLeave()