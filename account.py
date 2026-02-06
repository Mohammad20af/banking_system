class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return False

        else:
            self.balance += amount
            self.transactions.append(f"Deposit:{amount}")
            print(f"{amount} deposited , your balance is {self.balance}")
            return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return False

        elif amount > self.balance:
            print("Invalid amount")
            return False

        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw:{amount}")
            print(f"{amount} withdrawn , your balance is {self.balance}")
            return True

    def show_transactions(self):
        if not self.transactions:
            print("No transactions")

        else:
            print(f"Transactions:{self.transactions}")
            for transaction in self.transactions:
                print(f"{transaction}")

    def to_dict(self):
        return {
            "name": self.name,
            "balance": self.balance,
            "transactions": self.transactions
        }