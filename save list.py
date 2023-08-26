import pickle

file_name = "list.pkl"

# Load the list from the file, or create a new list if the file doesn't exist
try:
    with open(file_name, "rb") as f:
        list = pickle.load(f)
except FileNotFoundError:
    list = []

while True:
    print("List manager:")
    choice = input("Do you want to view, add, or edit: ")
    if choice == "view":
        print(list)
    elif choice == "add":
        add = input("What is the name of the new item: ")
        list.append(add)
        print(list)
    elif choice == "edit":
        edit = input("Do you wish to delete the item or edit the name of the item: ")
        if edit == "delete":
            item = input("What is the name of the item you wish to delete: ")
            if item in list:
                list.remove(item)
                print(list)
            else:
                print("Item not found")
        elif edit == "edit":
            item = input("What is the name of the item you wish to edit: ")
            if item in list:
                new_item = input("What is the new name of the item: ")
                list[list.index(item)] = new_item
                print(list)
            else:
                print("Item not found")
        else:
            print("Invalid choice")
    else:
        print("Invalid choice")
    
    # Save the list to the file
    with open(file_name, "wb") as f:
        pickle.dump(list, f)
    
    if input("Do you wish to continue: ") == "yes":
        continue
    elif input("Do you wish to continue: ") == "no":
        exit()
    else:
        print("Invalid choice")
