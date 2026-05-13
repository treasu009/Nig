# Parent class
class Account:
    def __init__(self, balance):
        self.balance = balance

    # Default withdrawal method
    def withdraw(self, amount):
        self.balance -= amount
        print(f"${amount} withdrawn successfully")


# Child class
class SavingsAccount(Account):

    def __init__(self, balance):
        super().__init__(balance)

        # 1. Withdraw limit attribute
        self.withdraw_limit = 100

    # 2. Override withdrawal behavior
    def withdraw(self, amount):

        if amount > self.withdraw_limit:
            print("Withdrawal failed! Amount exceeds $100 limit.")

        elif amount > self.balance:
            print("Insufficient balance.")

        else:
            self.balance -= amount
            print(f"${amount} withdrawn successfully")


# Test
acc = SavingsAccount(500)

acc.withdraw(50)    # Allowed
acc.withdraw(150)   # Not allowed

print("Remaining Balance:", acc.balance)