class Banking:
    def __init__(self,acc_no:int,name:str,balance:int=0)->None:
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self,amount:int):
        self.balance += amount
        self.show_balance()

    
    def show_balance(self)->None:
        print(f"Bank balance of account (self.acc_no) is Rs.{self.balance}")
    
    def withdraw(self,amount:int):
        if amount>self.balance:
            print("Not enough Balance")
        else:
            self.balance -= amount
            self.show_balance()

    def transfer(self, to_account:'Banking',amount):
        to_account.balance += amount
        self.balance -= amount

    
acc1 = Banking(1,"sjasji",100)
acc1.deposit(1000)
acc1.withdraw(200)

acc2 = Banking(2,"vandana",0)
acc1.transfer(acc2,300)

acc1.show_balance()
acc2.show_balance()