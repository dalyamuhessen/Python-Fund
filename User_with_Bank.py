class BankAccount:
    def __init__(self, int_rate, balance=0):  
        self.balance = balance
        self.int_rate = int_rate
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def get_balance(self):
        print(f"Account balance: ${self.balance:.2f}")


class User:
    def __init__(self,name):
         self.name=name
         self.accounts={}
    def open_account(self,account_name,int_rate,balance=0):
         self.accounts[account_name]=BankAccount(int_rate,balance)
         print(f"Account '{account_name}' opened for{self.name}." )
         return self
    def make_deposit(self,amount,account_name):
         self.accounts[account_name].deposit(amount)
         return self
    def make_withdrawal(self, amount, account_name):
          self.accounts[account_name].withdraw(amount)
          return self
    def display_user_balance(self, account_name):
     self.account = self.accounts[account_name]
     print(f"User: {self.name} | Account: '{account_name}' | Balance: ${self.account.balance:.2f}")                                                            
     return self
    
    def transfer_money(self, other_user, amount, from_account, to_account):
        if amount > self.accounts[from_account].balance:
            print(f"Insufficient funds in '{from_account}' to transfer.")
        else:
            self.accounts[from_account].withdraw(amount)
            other_user.accounts[to_account].deposit(amount)
            print(f"{self.name} transferred ${amount} from '{from_account}' to {other_user.name}'s '{to_account}'.")
        return self
    

user1=User("Mohammed")
user2=User("Shara")

user1.open_account("Savings",0.05,500)
user1.open_account("Checking",0.03)
user2.open_account("Checking",0.02)
print()

user1.make_deposit(300, "Checking")\
     .make_deposit(600, "Checking")\
     .make_deposit(100, "Checking")\
     .make_withdrawal(190, "Checking")\
     .display_user_balance("Checking")
user1.make_deposit(300, "Savings")\
     .make_deposit(800, "Savings")\
     .display_user_balance("Savings")
 
user2.make_deposit(200, "Checking")\
   .make_deposit(90,  "Checking")\
   .make_withdrawal(700, "Checking")\
   .display_user_balance("Checking")
 
user1.transfer_money(user2,300, "Checking", "Checking")
user1.display_user_balance("Checking")
user2.display_user_balance("Checking")
 