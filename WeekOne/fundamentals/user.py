# make a user class
class bank_member:
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name

    def withdrawal(self, number):
        self.balance -= number
        return self

    def deposit(self, number):
        self.balance += number
        return self
    
    def print_info(self):
        print(self.balance)
        print(self.name)

    def transfer(self, number, user):
        self.balance -= number
        user.balance += number
        return self


#the user needs to have a name, account balance

user1 = bank_member(100, "Ben")
user2 = bank_member(50, "Aaron")

user1.print_info()
user1.withdrawal(10)
print('_________________________')
user1.print_info()
user2.print_info()
user1.transfer(10, user2).withdrawal(10)
print('_________________________')
user1.print_info()
user2.print_info()