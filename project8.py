#PASSWORD AND USERNAME CHECKER
while True:
    name = input("Enter a name for login: ")
    names = name.split()
    for i in names:
        if i.isnumeric():
            print("Wrong Input! ")
            break
        elif i.isalpha():
            continue
        else:
            print("Wrong input! ")
            break
    password = input("Enter a password for login: ")
    passwords = password.split()
    counter=0
    try:
        if passwords[1]:
            print("Wrong password! ")
            continue
    except IndexError:
        pass
    if len(passwords) > 6:
        print("Wrong password! Password lenght cant be more than 8 characters! ")

    if password.isalpha():
        print("Login successful! ")
    else:
        print("Password should have numbers as well as digits!")




