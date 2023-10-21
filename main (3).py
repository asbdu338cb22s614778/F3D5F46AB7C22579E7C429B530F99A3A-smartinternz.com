

class Bank_Account:
  def __init__(self):
      self. balance=0
      print("Hello!!!the Deposit & withdrawal Machine")
  
  def deposit(self):
    amount=float(input("Enter The amount to be Deposited:"))
    self.balance+=amount
    print("\n Amount Deposited:", amount)
  
  def Withdraw(self):
    amount=float(input("Enter the amount to be withdraw:"))
    if self. balance>=amount:
       self. balance-=amount
       print("\n You Withdraw:", amount)
    else:
      print("\n Insufficient balance ")
  
  def display(self):
     print(" \n Account Balance=",self.balance)
  
#Driver code

# create an object of class
s = Bank_Account()
  
#calling function with that class object    
s.deposit()
s.Withdraw()
s.display()

