# Define balance
# Choose operation
# Perform deposit or withdrawal
# Show transaction history
# Exit program

history = []
balance = 200
password = "1905"


entered_password = input("Enter your password: ")
if not entered_password == password:
    print("Wrong password entered. Access denied.")
else:
    while True:
        # operation menu
        print("Select an operation: \n1- Show balance\n2- Deposit money\n3- Withdraw money\n4- Transaction history\n5- Exit")

        # Get user choice
        operation = int(input("Enter the number of your operation: "))

        # validate choice
        if operation < 1 or operation > 5:
            print("Please enter a valid number.")
        else:
            print("Processing your request.")

        # perform operation

        if operation == 1:
            print(f"Your balance: {balance}")
            print("Returning to main menu...")
        elif operation == 2:
            deposit_amount = int(input("Enter the amount you want to deposit: "))
            balance += deposit_amount
            history.append(f"{deposit_amount} deposited. New balance: {balance}")
            print("Returning to main menu...")
        elif operation == 3:
            withdraw_amount = int(input("Enter the amount you want to withdraw: "))
            if withdraw_amount > balance:
                print("Insufficient funds.")
                print("Returning to main menu...")
            else:
                print(f"Preparing your cash...")
                balance -= withdraw_amount
                history.append(f"{withdraw_amount} withdrawn. New balance: {balance}")
                print("Returning to main menu...")
        elif operation == 4:
            print("Showing transaction history:\n")
            for item in history:
                print(item)
            print("Returning to main menu...")
        else:
            print("Exiting... Goodbye!")
            break
