from file_handeler import load_data
from helpers import login_user, create_user,show_top_balance,update_user

def main():
    users_data = load_data()
    while True:
        print("--- Mini Banking System ---")
        print("1- login user ")
        print("2- create account")
        print("3- show top balance")
        print("4- exit")
        choice = input("enter your choice: ")

        if choice == "1":
            user = login_user (users_data)
            if user:
                while True:
                    print(f"\Welcome{user.username}")
                    print("1- Deposit")
                    print("2- Withdraw")
                    print("3- show_transactions")
                    print("4- logout")
                    sub_choice = input("Enter your choice: ")
                    if sub_choice == "1":
                        amount = float(input("Enter deposit amount:"))
                        user.account.deposit(amount)
                        update_user(users_data, user)
                    elif sub_choice == "2":
                        amount = float(input("Enter withdrawal amount: "))
                        user.account.withdraw(amount)
                        update_user(users_data, user)
                    elif sub_choice == "3":
                        user.account.show_transactions()
                    elif sub_choice == "4":
                        print("logged out")
                        break
                    else:
                        print("Inveiled choice!")
        elif choice == "2":
            create_user(users_data)
        elif choice == "3":
            show_top_balance(users_data)
        elif choice == "4":
            print("goodbye")
            break
        else:
            print("Inveiled choice!")

if __name__ == "__main__":
    main()
