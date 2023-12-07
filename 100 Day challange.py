import random
while True:
    try:
        lenght = int(input("How long do you want the password to be: "))
    except ValueError:
        print("Please enter a valid number")
lenght = len