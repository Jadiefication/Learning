class Contact:
    def __init__(self, name, number, surname):
        self.name = name
        self.number = number
        self.surname = surname
        
contacts = []        
        
while True:
    try:
        choice = input("Do you wish to view, add, remove or edit a contact(V/A/R/E): ")
    except choice != "V" or choice != "A" or choice != "R" or choice != "E":
        print("invalid choice")
    else:
        if choice == "a":
            contact_name = input("Enter the contact name: ")
            contact_surname = input("Enter the contact surname: ")
            try:
                contact_number = int(input("Enter the contact number: "))
            except ValueError:
                print("Please enter a valid contact number")
            else:
                new_contact = Contact(contact_name, contact_number, contact_surname)
                contacts.append(new_contact)
                try:
                    visibility = input("Do you wanna see your contacts(Y/N): ").strip().lower()
                except visibility != "y" or visibility != "n":
                    print("Please enter a valid choice")
                else:
                    if visibility == "y":
                        for contact in contacts:
                            print(f"Name: {contact.name}, Surname: {contact.surname}, Number: {contact.number}")
                    elif visibility == "n":
                        exit()

    
    
    