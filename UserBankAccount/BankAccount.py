class BankAccount:
    def __init__(self, int_rate, balance=0): 
        self.int_rate=int_rate
        self.balance=balance

    def deposit(self, amount):
        self.balance +=amount
        return self

    def withdraw(self, amount):
        if amount >self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -=5
        else:
            self.balance -=amount
        return self


    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self


    def yield_interest(self):
        if self.balance >0 :
            self.balance +=self.balance * self.int_rate
            return self
        


account1=BankAccount(0.05)
account1.deposit(500).deposit(200).deposit(400).withdraw(700).yield_interest().display_account_info()

account2 = BankAccount(0.03, 100)   
account2.deposit(300).deposit(200).withdraw(150).withdraw(100).withdraw(200).withdraw(1000).yield_interest().display_account_info()
