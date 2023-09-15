class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} successfully. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} successfully. New balance: {self.balance}")
        else:
            print("Insufficient balance.")
    
    def get_balance(self):
        return self.balance


# Create an instance of the BankAccount class
account = BankAccount("1234567890", 1000)

# Test deposit functionality
account.deposit(500)

# Test withdrawal functionality
account.withdraw(200)
account.withdraw(1500)

# Get current balance
balance = account.get_balance()
print(f"Current balance: {balance}")