
counter = 0
def userini():
    global counter
    name = input("Enter your name: ")
    attend = input("Enter attendance(P/A): ").lower()
    if attend == "p":
        counter += 1
        print("Marked present")
    elif attend == "a":
        print("Marked absent")
    else:
        print("Please enter a valid input")


while True:
    choice = input("Add student(View present/Add Student)").lower()
    if choice == "view present":
        print("Number of students present:" , counter)

    elif choice == "add student":
        userini()
    else:
        print("Please enter a valid input")
