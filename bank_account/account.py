class InsufficientFundsError(Exception):
    pass


class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.balance:
            raise InsufficientFundsError("Not enough funds")
        self.balance -= amount

    def __str__(self):
        return f"{self.owner}: {self.balance}"


if __name__ == "__main__":
    account = Account("Ali", 100)
    print(account.owner, account.balance)
