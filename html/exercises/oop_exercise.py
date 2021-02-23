####################################################
####################################################
# Object Oriented Programming Challenge - Solution
####################################################
####################################################
#
# For this challenge, create a bank account class that has two attributes:
#
# * owner
# * balance
#
# and two methods:
#
# * deposit
# * withdraw
#
# As an added requirement, withdrawals may not exceed the available balance.
#
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.


class Account:
    """
    Account object

    @param owner(str)
    
    @param balance(int)
    """
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print("Deposited: {0} successfully!Your current balance is {1}".format(amount, self.balance))
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Hello {1}.You do not have enough funds in your account to make this withdrawal.Your current balance is {0}".format(self.balance, self.owner))
        else:
            self.balance -= amount
            print("Withdrawn {0} successfully!Your current balance is {1}".format(amount, self.balance))
            return self.balance


# 1. Instantiate the class
acct1 = Account('Jose',100)


# 2. Print the object
print(acct1)


# 3. Show the account owner attribute
print(acct1.owner)


# 4. Show the account balance attribute
print(acct1.balance)


# 5. Make a series of deposits and withdrawals
acct1.deposit(50)


acct1.withdraw(75)


# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)


# ## Good job!
