import os
from user import User
from database import Database
from utils import clear_screen, pause

DB_FILE = "users.db"

def main_menu():
    clear_screen()
    print("=" * 30)
    print(" Welcome to Python ATM ")
    print("=" * 30)
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    return input("Select option: ")

def user_menu():
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Change PIN")
    print("5. Account Details")
    print("6. Logout")
    return input("Choose an option: ")

def register(db):
    clear_screen()
    print("--- Register New Account ---")
    name = input("Enter your name: ").strip()
    while True:
        pin = input("Set a 4-digit PIN: ")
        pin2 = input("Confirm PIN: ")
        if pin == pin2 and pin.isdigit() and len(pin) == 4:
            break
        print("PINs do not match or invalid. Try again.")
    user = db.create_user(name, pin)
    if user:
        print(f"\nAccount created successfully! Your Account No is: {user.account_no}")
    else:
        print("Registration failed.")
    pause()

def login(db):
    clear_screen()
    print("--- Login ---")
    acc = input("Enter Account No: ").strip()
    pin = input("Enter PIN: ").strip()
    user = db.authenticate(acc, pin)
    if not user:
        print("Invalid credentials!")
        pause()
        return None
    print(f"\nWelcome, {user.name}!")
    return user

def atm_session(user, db):
    while True:
        choice = user_menu()
        if choice == '1':
            print(f"\nCurrent Balance: ${user.balance:.2f}")
        elif choice == '2':
            amt = input("Enter amount to deposit: ")
            if amt.replace('.', '', 1).isdigit():
                amt = float(amt)
                if user.deposit(amt):
                    db.update_user(user)
                    print("Deposit successful.")
                else:
                    print("Minimum deposit amount is 1.")
            else:
                print("Invalid amount.")
        elif choice == '3':
            amt = input("Enter amount to withdraw: ")
            if amt.replace('.', '', 1).isdigit() and float(amt) > 0:
                if user.withdraw(float(amt)):
                    db.update_user(user)
                    print("Withdraw successful.")
                else:
                    print("Insufficient funds.")
            else:
                print("Invalid amount.")
        elif choice == '4':
            old = input("Enter current PIN: ")
            new = input("Enter new 4-digit PIN: ")
            if user.change_pin(old, new):
                db.update_user(user)
                print("PIN changed successfully.")
            else:
                print("Failed to change PIN.")
        elif choice == '5':
            print(f"\nAccount No: {user.account_no}")
            print(f"Name: {user.name}")
            print(f"Balance: ${user.balance:.2f}")
        elif choice == '6':
            print("Logging out...")
            pause()
            break
        else:
            print("Invalid option.")
        pause()

def main():
    db = Database(DB_FILE)
    while True:
        choice = main_menu()
        if choice == '1':
            register(db)
        elif choice == '2':
            user = login(db)
            if user:
                atm_session(user, db)
        elif choice == '3':
            print("Thank you for using Python ATM!")
            break
        else:
            print("Invalid option.")
            pause()

if __name__ == "__main__":
    main()