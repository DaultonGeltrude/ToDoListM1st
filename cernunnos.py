tasks = []

def addItem():
    task = input("---Enter Item> ")
    tasks.append(task)

def viewItem():
    if not tasks:
        print("---Nothing to Display---")
    else:
        print("---List---")
        for index, task in enumerate(tasks):
            print(f"Item #{index}. {task}")

def deleteItem():
    viewItem()
    try:
        itemToRemove = int(input("---Enter # "))
        if itemToRemove >=0 and itemToRemove < len(tasks):
            tasks.pop(itemToRemove)
            print("---Item Removed---")
        else:
            print("---INVALID INPUT---")
    except:
        print("---ERROR---")

if __name__ == "__main__":
    while True:
        print("\n Select an Input>")
        print('----------------------------------------')
        print('1. Add')
        print('2. Delete')
        print('3. View')
        print('4. Exit')
        print('----------------------------------------')

        choice = input("> ")

        if(choice == "1"):
            addItem()
        elif(choice == "2"):
            deleteItem()
        elif(choice == "3"):
            viewItem()
        elif(choice == "4"):
            break
        else:
            print('---FATAL ERROR---')

    print("---Session Ended---")
