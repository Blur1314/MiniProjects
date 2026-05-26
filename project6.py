items = {}
counter = 0
def additems():
    global counter
    iname = input("Enter item name: ")
    iquan = int(input("Enter item quantity: "))
    iprice = int(input("Enter item price: "))
    counter += 1
    item = {"name":iname,"quan": iquan,"price": iprice , "total" : iprice*iquan}
    items[counter] = item
    return item

def viewall():
    if items != {}:
        for key, value in items.items():

            print("Name:",value["name"],"Quantity",value["quan"],"Price:",value["price"],"Total:",value["total"],"\n")
    else:
        print("No items found")


while True:
    choice = input("Enter choice(ADD ITEMS/VIEW ALL): ").upper()
    if choice == "ADD ITEMS":
        additems()
    elif choice == "VIEW ALL":
        viewall()

    else:
        print("Invalid choice")