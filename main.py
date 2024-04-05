from admin import Admin
from bank import Bank
from user import User

def main(bank1, bank2):
    admin = Admin("Admin")

    while True:
        print("Choose your role:")
        print("1. Admin")
        print("2. Customer")
        print("3. Bank User")
        print("4. Exit")
        role = input("Enter your choice: ")

        if role == "1":
            admin_tasks(admin)
        elif role == "2":
            bank = choose_bank()
            if bank:
                username = input("Enter user name: ")
                user = find_user_by_name(username, bank)
                if user:
                    user_tasks(user, bank)
                else:
                    print("User not found. Create a user from your bank")
                    print("----------------------------------------------")
            else:
                print("Invalid bank selection.")
        elif role == "3":
            bank = choose_bank()
            if bank:
                bank_user_tasks(bank)
            else:
                print("Invalid bank selection.")
        elif role == "4":
            break
        else:
            print("Invalid choice. Please try again.")


def choose_bank():
    print("Choose the bank:")
    print("1. KVB")
    print("2. ICICI")
    bank_choice = input("Enter your choice: ")

    if bank_choice == "1":
        return bank1
    elif bank_choice == "2":
        return bank2
    else:
        return None


def admin_tasks(admin):
    while True:
        print("Admin Tasks:")
        print("1. View Bank Details")
        print("2. View Customer Details")
        print("3. View Amount")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            bank = choose_bank()
            if bank:
                print(admin.view_bank_details(bank))
                print("-------------------------------------------------")
            else:
                print("Enter proper details of the bank")
                print("-------------------------------------------------")
        elif choice == "2":
            bank = choose_bank()
            if bank:
                print(bank.view_all_customer_details())  
                print("-------------------------------------------------")
            else:
                print("Invalid bank selection.")
                print("-------------------------------------------------")
        elif choice == "3":
            bank = choose_bank()
            print(f"Available balance in {bank.name} bank is {bank.view_balance()}")
            print("-------------------------------------------------")
        elif choice == "4":
            print("-------------------------------------------------")
            break
        else:
            print("Invalid choice. Please try again.")


def user_tasks(user, bank):
    while True:
        pin = input("Enter your pin:")
        if pin == user.pin:
            print("Customer Tasks:")
            print("1. Withdraw")
            print("2. Deposit")
            print("3. View Balance")
            print("4. Mini Statement")
            print("5. Change Pin")
            print("6. Generate Pin")
            print("7. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                amount = int(input("Enter amount to withdraw: "))
                if user.withdraw(amount):
                    print("Withdrawal successful.")
                    print("-------------------------------------------------")
                else:
                    print("Insufficient balance.")
                    print("-------------------------------------------------")
            elif choice == "2":
                amount = int(input("Enter amount to deposit: "))
                user.deposit(amount)
                print("Deposit successful.")
                print("-------------------------------------------------")
            elif choice == "3":
                print("Current Balance:", user.view_balance())
                print("-------------------------------------------------")
            elif choice == "4":
                print("Mini Statement:", user.mini_statement())
                print("-------------------------------------------------")
            elif choice == "5":
                old_pin = input("Enter your old pin:")
                if old_pin == user.pin:
                    new_pin = input("Enter your new pin:")
                    if new_pin!=old_pin:
                        user.pin = new_pin
                        print("Pin changed successfully")
                        print("-------------------------------------------------")
                    else:
                        print("New pin cannot be same as the old pin")
                else:
                    print("Incorrect pin. Please check your pin or generate a new one.")
                    print("-------------------------------------------------")
            elif choice == "6":
                old_pin = input("Enter your old pin:")
                if old_pin == user.pin:
                    gen_pin = User.generate_pin()
                    print(f"You pin is:{gen_pin}")
                    print("-------------------------------------------------")
                else:
                    print("Incorrect pin. Please check your pin or generate a new one.")
                    print("-------------------------------------------------")
                    break
                

            elif choice == "7":
                print("-------------------------------------------------")
                break
            else:
                print("Invalid choice. Please try again.")
                print("-------------------------------------------------")
        else:
            print("Incorrect pin. Please check your pin or generate a new one.")


def bank_user_tasks(bank):
    while True:
        print("Bank User Tasks:")
        print("1. View Bank Details")
        print("2. Add user")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print(bank.view_details())
            print("-------------------------------------------------")
        elif choice == "2":
            u_name = input("Enter user name: ")
            if not find_user_by_name(u_name, bank):
                pin = input("Enter your pin:")
                user = User(u_name, pin, bank.gen_acc_no(), bank)
                bank.add_user(user)
                print(f"User added successfully. The details are mentioned below:\n{user.mini_statement()}")
                print("-------------------------------------------------")
            else:
                print("User name already exists")
                print("-------------------------------------------------")
        elif choice == "3":
            print("-------------------------------------------------")
            break
        else:
            print("Invalid choice. Please try again.")
            print("-------------------------------------------------")

def find_user_by_name(username, bank):
    for user in bank.users:
        if user.name == username:
            return user
    return None

if __name__ == "__main__":

    bank1 = Bank("KVB", 0,0000)
    bank2 = Bank("ICICI", 0,0000)
    
    main(bank1, bank2)
