
class User:
    def __init__(self, username, password, account):
        self.username = username
        self.password = password
        self.account = account

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "account": self.account.to_dict()
        }
