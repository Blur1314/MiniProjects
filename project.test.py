

tasks = {"id" :None ,"Name" : None , "start": None , "end" : None , "Status" : None }

dict = {}
counter = 1
while True:
    role = input("Enter a role (Service Coordinator/ Engineer)")
    if role == "Service Coordinator" :
        temp = input("what do you want to perform (Add task/Show status): ")
        if temp == "Add task" :
            tasks = {"id" :None ,"Name" : None , "start": None , "end" : None , "Status" : None }
            nme  = input("Enter a name")
            tasks["Name"] = nme
            start = input("Enter a start date")
            end = input("Enter a end date")
            tasks["start"] = start
            tasks["end"] = end
            tasks["id"] = counter
            dict[counter] = tasks
            counter += 1
        elif temp == "Show status" :
            print("Enter a name")
            for i in range(len(dict)):
                print(f"{dict[i + 1]['Name']}")
            nameee = input("Enter a name:")
            for i in range(len(dict)):
                if dict[i + 1]['Name'] == nameee:
                    mainmann = dict[i + 1]["id"]
            print("task status for " , nameee ," is " , dict[mainmann]["Status"])
            """for i in range(len(dict)):
                
                print("Task status: ", dict[i+1]["Status"] , "-->" , dict[i+1]["Name"])"""
        else:
            print("Invalid input")
    if role == "Engineer" :
        print("Enter a name")
        for i in range(len(dict)):
            print(f"{dict[i+1]['Name']}")
        namee = input("Enter a name:")
        statuschange = input("Change status of task to ?: ")
        for i in range(len(dict)):
            if dict[i+1]['Name'] == namee :
                mainman = dict[i+1]["id"]

        dict[mainman]["Status"] = statuschange
        print("Thank you!")





