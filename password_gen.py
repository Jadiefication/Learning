import random, pickle, string
file_name = "password.txt"
lonG = int(input("How long do you want your password to be: "))
chars = string.ascii_lowercase + string.digits + string.ascii_uppercase
password = "".join(random.choice(chars) for _ in range(lonG))
print(password)
with open(file_name, "wb") as file:
    pickle.dump(password, file)
