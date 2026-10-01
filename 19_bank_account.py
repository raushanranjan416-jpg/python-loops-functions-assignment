balance = 0
transaction_history = []
def deposit(amt: int):
    global balance
    balance += amt
    transaction_history.append({"action": "Deposit", "amount": amt})

def withdraw(amt: int):
    global balance
    balance -= amt
    transaction_history.append({"action": "Withdraw", "amount": amt})


def check_balance():
    print("Available Balance is Rs ", balance)

def transaction_history_fn():
    if len(transaction_history) == 0:
        print("No Transaction Found")

    for txn in transaction_history:
        print(f"mode: {txn['action']}, Amount: Rs {txn['amount']}")

    print("Available Balance is Rs ", balance)


while True:
    try:

        print("== Welcome to Bank ===")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Check Transaction History")
        print()
        print()

        choice = int(input("Choose Option between 1 to 4"))

        if choice == 1:
            amt = int(input("Enter amount to deposit"))
            if amt <= 0:
                print("Amount is less than zero. Please")
                continue

            deposit(amt)
        elif choice == 2:
            amt = int(input("Enter amount to withdraw"))
            if amt <= 0 :
                print("Amount is less than zero. Please amount greater than 0")
                continue
            elif amt > balance:
                print("Insufficient Balance. Please amount to withdaw")
                continue

            withdraw(amt)
        elif choice == 3:
            check_balance()
        elif choice == 4:
            transaction_history_fn()
        elif choice == 5:
            break


    except ValueError:
        print("Error: Please enter a valid choice between 1 to 4")
    