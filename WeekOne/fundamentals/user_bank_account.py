class BankAccount:
    def __init__(self, balance = 100):
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
        print(f"you have $ {int(self.balance)} available.")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * .06
        return self

class BankMember:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(10)

    def withdrawal(self, number):
        self.account.withdrawal(number)
        return self
    
    def print_info(self):
        self.account.display_account_info()
        print(self.name)
    
    def deposit(self, number):
        self.account.deposit(number)
        return self

    # def transfer(self, number, user):
    #     self.balance -= number
    #     user.balance += number
    #     return self

Ben = BankMember("Ben")
Ben.print_info()
print("________________")
Ben.deposit(20).withdrawal(5).print_info()