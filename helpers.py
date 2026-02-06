from user import User
from account import Account
from file_handeler import save_data

def create_user(users_data):
    username=input("Enter your username: ")
    if username in users_data:
        print("Username already exists")
        return None
    else:
        password = input("Enter your password: ")
        account_number=len(users_data)+1
        user=User(account_number,username,password)
        users_data[username] = user.to_dict()
        save_data(users_data)
        print(f"User created successfully{account_number}")
        return user

def login_user(user_data):
    username=input("Enter your username: ")
    password=input("Enter your password: ")
    user_data=user_data.get(username)
    if not user_data :
        print("User does not exist")
        return None
    elif password != user_data.get["password"]:
        print("Incorrect password")
        return None
    account_data=user_data["account"]
    account=Account(account_data["account_number"],account_data["balance"])
    account.transactions=account_data.get("transactions",[])
    user=User(username,password,account)
    print("User logged in")
    return user

def update_user(users_data,user):
    users_data[user.username] = user.to_dict()
    save_data(users_data)

def show_top_balance(user_data):
    all_users=[]
    for user in user_data.values():
        account=user["account"]
        all_users.append((user["username"],account["balance"]))
    all_users.sort(key=lambda x:x[1],reverse=True)
    print("top balance :")
    for username,balance in all_users:
        print(f"{username} : {balance}")