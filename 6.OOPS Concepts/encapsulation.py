#Data hiding, public,private,and protected __ for private
class Father:
    def __init__(self,father_name,balance)-> None:
        self.father_name = father_name
        self.balance = balance
    def withdraw_balance(self,amount:int):
        if amount> self.balance:
            print("Not enough balance")
        else:
            self.balance -= amount
            print(f"withdraw rs.{amount},Remaining balance = rs.{self.balbance}")
    def deposit(self,amount:int):
        self.balance += amount
        print(f"Deposit Rs.{amount},Remaing balance = rs.{self.balance}")
    
class Child(Father):
    def __init__(self, father_name:str , balance: int , child_name:str)->None:
        super().__init__(father_name,balance)
        self.child_name = child_name

child= Child("sanjay",1000,"Anirudh")
print(child.balance)
child.balance = 10000
print(child.balance)