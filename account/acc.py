class Account:

    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance=self.balance - amount
        
    def deposit(self, amount):
        self.balance=self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

#inheritance - create sub class out of base class
#sub class shares methods of base class plus has its own
class Checking(Account):
    """This class generates checking account objects"""

    type="checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        #make fee global
        self.fee=fee

    def transfer(self, amount):
        self.balance=self.balance-amount - self.fee

#this is starting from the current working directory
# import os
# cwd = os.getcwd()
# print(cwd)
jacks_checking = Checking("account\\jack.txt", 1)
jacks_checking.deposit(100)
jacks_checking.transfer(50)
print(jacks_checking.balance)
jacks_checking.commit()


johns_checking = Checking("account\\john.txt", 1)
johns_checking.deposit(100)
johns_checking.transfer(50)
print(johns_checking.balance)
johns_checking.commit()

#examples of how to use the class
# account=Account("account\\balance.txt")
# print(account.balance)
# account.withdraw(100)
# account.deposit(50)
# print(account.balance)
# account.commit()