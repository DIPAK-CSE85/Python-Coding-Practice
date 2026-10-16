print("***WELLCOME TO INFINITY CREST BANK***")
class BankAccount:
    def __init__(self,name,balance=0):
        self.holdername=name
        self.balance=balance
    def deposite(self,amount):
        self.balance+=amount  
        print(f"Deposited {amount} to your account")  
        print(f"total balance:{self.balance}")    
    def withdraw(self,amount):
        if amount>self.balance:
            print("NOT ENOUGH BALANCE IN YOUR ACCOUNT,PLESE TRY AGAIN AND ENETR LESS AMOUNT")    
        else:
            self.balance-=amount
            print("withdraw successfuly")
            print(f"Remaining Balance In Your Account:{self.balance}")
            print("***THANK YOU***")
    def __str__(self):
        return f"ACCOUNT HOLDER NAME:{self.holdername}\nBALANCE:{self.balance}"    
holder=BankAccount(input("PLESE ENTER YOUR NAME:"),10000)
print(holder)
holder.deposite(int(input("ENTER A DEPOSITE AMOUNT:")))
holder.withdraw(int(input("ENTER A WITHDRAW AMOUNT:")))  
 
        