#inheriting a class from another class
#it can use all the methods and parameters from parent class
class Animal:
    def __init__(self,name:str,color:str,age:int)->None:
        self.name = name
        self.age = age
        self.color = color

    def eat(self):
        print("i am eating")

    def sleep(self):
        print("i am sleeping")
    
class Sparrow(Animal):
    def __init__(self,name:str,color:str,age:int,city:str,state:str):
        super().__init__(name,color,age)
        self.city = city
        self.state = state
    def fly(self):
        print("im flying")
    def display_info(self):
        print(f"city = {self.city},state = {self.state}")
        print(f"name={self.name}, color ={self.color}, age ={self.age}")


s= Sparrow("jackey","broun",3,"surat","guj")
s.display_info()
s.fly()
s.eat()
s.sleep()
