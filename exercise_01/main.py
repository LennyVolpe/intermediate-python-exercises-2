from BankAccount import BankAccount

bank1=BankAccount("jaonh" ,1000)

bank1.withdraw(500)
bank1.deposit(1000)

print(bank1.get_balance())