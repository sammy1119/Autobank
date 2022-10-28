class CustomerAccount:
    """This is an ecobank account"""

    def __init__(self, balance=0.0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, withdrawal):
        self.balance -= withdrawal

    def check_balance(self):

        return self.balance
