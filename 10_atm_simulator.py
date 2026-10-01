
balance = 10000

while True:
    try:
        print("=== Welcome to Atm Machine ===")
        print("1. Check Balance")
        print("2. withdraw money")
        print("3. deposit money")
        print("4. exit")
        choice = int(input("Enter your choice between 1 to 4"))

        if choice == 1:
            print(f"Balance: Rs {balance}")
        
        elif choice == 2:
            amount = int(input(f"Enter amount to withdraw"))
            if amount < 0 :
                print(f"Please enter valid amount to withdraw. Amount can not be negative")
                continue
            elif amount > balance:
                print(f"Insufficient Balance, Balance is : Rs {balance}")
                continue


            balance = balance - amount
            print(f"Available Balance: {balance}")
        
        elif choice == 3:
            amount = int(input(f"Enter amount to deposit"))
            if amount < 0 :
                amount = int(input(f"Please enter valid amount to deposit "))

            balance = balance + amount
            print(f"Available Balance: {balance}")

        elif choice == 4:
            print(f"=== Thank you ===")
            break
        
        else :
            print("Enter valid Choice.")

    except ValueError:
        print("Error: Please enter a valid choice")


        

