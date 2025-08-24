from database import userbase 

def checkUser():
    name_in = input("What's your name? ")
    # now check
    for key, value in userbase.items():
        if value.get("name") == name_in:
            pass
        else:
            print("User not found.\n")
            checkUser()
        return name_in

active_user = checkUser()

def checkPassword():
    passwd_in = input("What's your password? ")
    # now check
    for key, value in userbase.items():
        if value.get("password") == passwd_in:
            pass
        else:
            print("Incorrect password.\n")
            checkPassword()
        return passwd_in

active_user_password = checkPassword()


#Welcome user
print("Welcome ", active_user)

