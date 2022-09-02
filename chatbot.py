# Chatbot for social networking site
import getpass as gp

database = {"aryan.gupta": "123456", "devil.28": "789456"}


def report():
    username = str(input("Enter the username that you want to report: "))
    print("Explicit content")
    print("Abusing")
    print("Customise")
    choice = str(input("Enter the reason: "))

    if choice.lower() == "customise":
        customize = str(input("Enter the reason:"))

    print("We'll reach back to you after reviewing all the details")


def deactivate():
    username = str(input("Enter your username: "))
    password = gp.getpass("Enter your password: ")

    for i in database.keys():
        if username == i:
            while password != database.get(i):
                print("Incorrect Password")
                password = gp.getpassword("Enter the password again: ")

            if password == database.get(i):
                print("Verified")
                choice = str(input("Enter Y to deactivate or N to stop: "))

                if choice.lower() == "y":
                    print("We are going to deactivate your account")
                    break
                else:
                    print("Deactivation cancelled")
                    break
        else:
            print("Username incorrect")
            break


def other():
    query = input("Please enter your query: ")
    print("Thanks for coming! Our team will reach back to you shortly")


    # **********************************************************************************
print("Welcome")
print("Bot- Hi! how can I help?")

while True:
    print("Report an account")
    print("Deactivate my Account")
    print("Other query")
    print("exit")
    ans = str(input("user-"))

    if ans.lower() == "report an account":
        report()

    elif ans.lower() == "deactivate my account":
        deactivate()

    elif ans.lower() == "other query":
        other()

    elif ans.lower() == "exit":
        break

print("Sorry for the inconvenience. We hope it solved your problem")
print("Feel free to reach out")
