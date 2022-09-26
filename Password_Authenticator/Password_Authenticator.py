import getpass
database = {"saiashish": "123456", "konchada": "654321"}

username = input("Enter username: ")

if username in database :
    password = getpass.getpass(prompt="Enter your password: ")
    if database[username] == password :
        print ("You are now logged into the system.")
    else :
        print ("Invalid password.")
else :
    print ("You are not valid user.")
