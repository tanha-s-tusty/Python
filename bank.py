class Bank:
    bank_name = "Grameen Bank"
    # constructor
    def __init__(self,acc_num:int,name:str,balance:int):
        self.acc_num = acc_num
        self.name = name
        self.balance = balance
    # deposit ammount
    def deposit(self,amount):
        if amount<=0:
            return "amount negetive or Zero -invalid"
        self.balance +=amount
        return f"Deposit Successful,amount {amount},current balance {self.balance}"
    # withdraw amount
    def withdraw(self,amount):
        if amount > self.balance:
            return "Withdraw Failed - insufficient funds"
        self.balance -=amount
        return f" Withdraw successful,amount {amount},current balance {self.balance}"
    # display account info
    def display(self):
        return f"{Bank.bank_name} Account number {self.acc_num} name {self.name} current balance {self.balance:.2f}"

# creating bank object / user
p1 = Bank(1999,"Y",743025)

print(p1.deposit(2643))
print(p1.withdraw(93621))

print(p1.display())
