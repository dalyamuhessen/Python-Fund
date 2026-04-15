class User :
    def __init__ (self,name,balance=0):
       self.name=name
       self.balance=balance
    def make_deposit(self,amount):
       self.balance +=amount
    def make_withdrawal(self,amount):
        if amount>self.balance:
           print(f"Insufficient funds for {self.name} . Curent balance: ${self.balance}")
        else:
           self.balance -=amount
    
    def display_user_balance(self):
      print(f"User:{self.name}, Balance:${self.balance}")
    def transfer_money(self,other_user,amount):
       if amount>self.balance:
          print(f"Insufficient funds to transfer. {self.name}'s balance: ${self.balance}")
       else:
          self.balance -=amount
          other_user.balance+=amount
          print(f"{self.name} transferred ${amount} to {other_user.name}.")


user1=User("Ola N Shawa")
user2=User("Alaa M Mzainy")
user3=User("Dalya S Mohusen")

user1.make_deposit(100)
user1.make_deposit(200)
user1.make_deposit(130)
user1.make_withdrawal(34)
user1.display_user_balance()

user2.make_deposit(300)
user2.make_deposit(150)
user2.make_withdrawal(100)
user2.make_withdrawal(24)
user2.display_user_balance()


user3.make_deposit(200)
user3.make_withdrawal(120)
user3.make_withdrawal(200)
user3.make_withdrawal(10)
user3.display_user_balance()


user1.transfer_money(user3,200)
user1.display_user_balance()
user3.display_user_balance()