def checkInput():
    correctUsername = "eric"
    correctPassword = "1234"

    inputUsername = input("Username: ").lower()
    inputPassword = input("Password: ")

    if (inputUsername == correctUsername and inputPassword == correctPassword):
        print("Welcome in User")
        
    else:
        print("Username or password is incorrect, try again\n")
        checkInput()

if __name__ == "__main__": 
    checkInput()