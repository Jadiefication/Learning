name = input("What is your name: ")
drugs = input("Are you on drugs: ")
if drugs == "yes":
    print("Okay ummm Im gonna call 911 so they can help you")
elif drugs == "no":
    question = input("Do you know someone on drugs: ")
    if question == "yes":
        Question = input("Who is the person: ")
        if Question == "":
            print("Ok then im  gonna call 911 on you for not complying")
        elif question == name:
            print("Why didnt you just say it from the start?")
        else:
            print("Thank you for your compliance", name)
else:
    print("Ok then im  gonna call 911 on you for not complying")