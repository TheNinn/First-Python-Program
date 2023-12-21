
def createuser():
    username = input("Enter your full name: ")
    firstname = username[: username.find(" ")]
    lastname = username[username.find(" ") + 1:]
    age = input("Enter your age: ")

    if username.find(" ") == -1:
        print("Please enter your full name")
    elif lastname == "":
        print("Please enter your full name")
    elif lastname == " ":
        print("Plese enter your full name")
    elif age.isdigit() == False:
        print("Please enter a valid age")
    else:
        age = int(age)
        with open("users.txt", "a") as file:
            file.write(f"Name: {firstname}\nLastname: {lastname}\nAge: {age}\n-----------------------------\n")
    createuser()
            

createuser()