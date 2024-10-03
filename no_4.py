# Qns. 4
# WITI Academy is proposing a sacco to help students save their money.
# Design a platform that will do the following.
# Welcome to, WITI Sacco
# deposit Money
# Withdraw Money 
# check Balance
# Ensure if the student selected 1, money is deposited and the minimum deposited should be 1000.
# if the student selects 2, money should be withdrawn and the minimum withdraw is 500.
# if the student selects 3, the account balance shold be displyed.

#soln
balance = 0

print("Welcome to WITIAcademy Sacco")
print("\nPlease choose an option:")
print("1. Deposit Money")
print("2. Withdraw Money")
print("3. Check Balance")

choice = input("Enter your choice (1/2/3): ")

if choice == '1':  
    amount = float(input("Enter amount to deposit: "))
    if amount >= 1000:
        balance += amount
        print(f"Successfully deposited {amount}. New balance is {balance}.")
    else:
        print("Minimum deposit amount is 1000.")

elif choice == '2': 
    amount = float(input("Enter amount to withdraw: "))
    if amount >= 500:
        if balance >= amount:
            balance -= amount
            print(f"Successfully withdrew {amount}. New balance is {balance}.")
        else:
            print("Insufficient balance.")
    else:
        print("Minimum withdrawal amount is 500.")

elif choice == '3':  # Check Balance
    print(f"Your current balance is {balance}.")

else:
    print("Invalid choice.")