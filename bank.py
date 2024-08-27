class Account:
  def __init__(self,name,acnum,bal):
    if not isinstance(name,str) or not name.isalpha():
      raise ValueError("ERROR:Name should be string")
    
    if not isinstance(acnum,int):
      raise ValueError("ERROr:Account number should be integer")
    
    self.usernm = name
    self.acnum = acnum
    self.bal = bal

  def __str__(self):
    return f"CustomerName :{self.usernm}  Account Number : {self.acnum} Balance : {self.bal}"
  def credit(self,amt):
    self.bal += amt
  def debit(self,amt):
    if amt > self.bal:
      print("Insufficient Balance")
    else:
      self.bal -= amt


class Bank:
  def __init__(self,name,address):
    self.accounts = []
    self.Name = name
    self.address = address
  def add_account(self,acc:Account):
    self.accounts.append(acc)

  def delete_account(self,acc:Account):
    self.accounts.remove(acc)

  def display(self):
    for acc in self.accounts:
      print(acc)
try:
    acc1 = Account('rutu',1234,4000)
    acc2 = Account('Raj',12345,5000)
    acc3 =Account('Ravi',1236,2300)

    b1 = Bank('SBI','Pune')
    b1.add_account(acc1)
    b1.add_account(acc2)
    b1.add_account(acc3)
    print("--Before deleting---")
    b1.display()
    b1.delete_account(acc2)
    print("--After deleting---")
    acc1.credit(2000)
    b1.display()

    acc1.credit(2000)
except ValueError as ve:
  print(ve)
except Exception as e:
    print(e)


      
 
  