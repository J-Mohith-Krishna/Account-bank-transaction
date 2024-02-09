class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount for withdrawal.")

    def check_balance(self):
        print(f"Current balance for {self.owner}: ${self.balance}")


if __name__ == "__main__":
    # Creating a new bank account
    account1 = BankAccount("John Doe", 1000)

    # Performing transactions
    account1.deposit(500)
    account1.withdraw(200)
    account1.check_balance()

    # Creating another account
    account2 = BankAccount("Jane Smith")

    # Performing transactions on the second account
    account2.deposit(2000)
    account2.withdraw(1000)
    account2.check_balance()
