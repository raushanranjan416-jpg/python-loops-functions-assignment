
Password = "Hello World"
attempt = 0

while True:
        if attempt >=3:
            print("Account Locked")
            break

        enter_password = input("Enter your password")
        if enter_password == Password:
            print("Login Successfull.")
            break
        
        else:
            print("Incorrect Password, try again.")
            attempt += 1
        



        

