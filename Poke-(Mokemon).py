valid_types = ["earth", "fire", "air", "water", "spirit"]
name = input("What is your beast's name: ")
while True:
    type = input("What is its type: ").strip().lower()
    if type in valid_types:
        break
    else:
        print("That is not a valid type. Please try again.")
special = input("What is his special move: ")
while True:
    hp = int(input("What is his HP: "))
    if hp <= 0:
        print("That is not a valid HP. Please try again.")
    elif hp >= 1000:
        print("That is not a valid HP. Please try again.")
    else:
        mp = int(input("What is his MP: "))
        if mp <= 0:
            print("That is not a valid MP. Please try again.")
        elif mp >= 1000:
            print("That is not a valid MP. Please try again.")
        else:
            break
beast = {"name": name, "type": type, "special": special, "hp": hp, "mp": mp}
if type == valid_types[0]:
    print(f"\033[32mYour beast is called {beast['name']}. It is an earth beast with a speacial move of {beast['special']}.\033[0m")
elif type == valid_types[1]:
    print(f"\033[31mYour beast is called {beast['name']}. It is an fire beast with a speacial move of {beast['special']}.\033[0m")
elif type == valid_types[2]:
    print(f"mYour beast is called {beast['name']}. It is an air beast with a speacial move of {beast['special']}.")
elif type == valid_types[3]:
    print(f"\033[34mYour beast is called {beast['name']}. It is an water beast with a speacial move of {beast['special']}.\033[0m")
elif type == valid_types[4]:
    print(f"\033[35mYour beast is called {beast['name']}. It is an spirit beast with a speacial move of {beast['special']}.\033[0m")