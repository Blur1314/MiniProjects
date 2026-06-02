meetings=[]


def addmeeting():
    mname = input("Enter Meeting name: ")
    mdate = input("Enter date of meeting: ")
    mtime = input("Enter time of meeting: ")
    curlst= [mname, mdate, mtime]
    meetings.append(curlst)
    return curlst

def viewall():
    if meetings != []:
        for i in meetings:
            print("Meeting Name" , i[0],"\nMeeting date",i[1],"\nMeeting time",i[2],"\n\n")
    else:
        print("No meetings found")

def conflict(clst):
    counter = 0
    for i in meetings:
        if clst[2] == i[2] and clst[1] == i[1]:
            counter +=1

        if counter == 2:
            print("Conflict , Meeting deleted from list! , Please enter another meeting!")
            return "CONFLICT"





while True:
    choice = input("What do you want to do(VIEW/ADD MEETING)): ").upper()
    if choice == "VIEW" :
        print(meetings)
        viewall()
    elif choice == "ADD MEETING":
        curlst = addmeeting()

        statement = conflict(curlst)
        if statement == "CONFLICT":
            meetings.remove(curlst)
        else:
            print("DONE")

    else:
        print("Invalid input")



