class BankAccount:
    def __init__(self, balance = int(100.00)):
        self.balance = balance
    
    def withdrawal(self, amount):
        if amount<=self.balance:
            self.balance -= amount
        else:
            print("insufficient funds")
        return self
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def display_account_info(self):
        print("you have","$"+str(self.balance),"available.")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * .06
        return self

user1 = BankAccount()
user1.display_account_info()
user1.yield_interest()
print("____________________")
user1.display_account_info().yield_interest().display_account_info()