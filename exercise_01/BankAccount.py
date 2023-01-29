class BankAccount:

    def __init__(self, account_name, starting_balance):

        self.account_name = account_name
        self.starting_balance = starting_balance

    def deposit(self, dep_amount):
        self.starting_balance += dep_amount
        return self.starting_balance

    def withdraw(self, with_amount):

        self.starting_balance-= with_amount
        return self.starting_balance

    def get_balance(self):
        return str(self.account_name) + " has a balance of " + str(self.starting_balance)




    





        