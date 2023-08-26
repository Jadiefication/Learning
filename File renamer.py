import os
path = input("Enter the path of the file: ")
if os.path.isfile(path):
    print("File exists")
    rename = input("Do you want to rename the file? (y/n): ")
    if rename == "y":
        newname = input("Enter the new name: ")
        os.rename(path, newname)
        print("File renamed")
    elif rename == "n":
        l = input("Do you want to delete the file? (y/n): ")
        if l == "y":
            os.remove(path)
            print("File deleted")
        elif l == "n":
            print("File not deleted")
        else:
            print("Invalid input")
    else:
        print("Invalid input")