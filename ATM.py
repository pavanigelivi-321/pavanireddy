balance = 0   # Initial balance

# Function to deposit money
def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    
    if amount > 0:
        balance += amount
        print("Amount deposited successfully!")
    else:
        print("Invalid amount!")

# Function to withdraw money
def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    
    if amount <= balance:
        balance -= amount
        print("Please collect your cash.")
    else:
        print("Insufficient balance!")

# Function to check balance
def check_balance():
    print("Current Balance:", balance)

# Main program
while True:
    print("\n--- ATM Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        deposit()
    elif choice == 2:
        withdraw()
    elif choice == 3:
        check_balance()
    else:
        print("Invalid choice!")

    again = input("Do you want to continue? (y/n): ")
    if again.lower() != 'y':
        print("Thank you for using ATM!")
        break