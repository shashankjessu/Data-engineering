#six main pillers
# 1.classes 2.objects3.inheritence 4.polymorphism 5.obstracton 6 encapsulation

class Student:
    roll_no:int =0
    name:str = ""
    age:int = 0
    standard:str = ""

    #constructor method
    def __init__(self,roll_no:int,name:str,age:int,standard:str):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.standard = standard
        self.school = 'dps'


    #methods
    # def set_information(self):
    #     self.roll_no = int(input("Enter a roll_no ="))
    #     self.name = input("Enter a name =")
    #     self.age = int(input("Enter a age ="))
    #     self.standard = int(input("Enter a standard ="))

    # def display(self): #current instance of the class.instance mean object 
    #     print(
    #         f"Roll no = {self.roll_no}, Name = {self.name} , Age = {self.age}, Standard = {self.standard}"
    #     )

    #parameters for the same above
    # def set_information(self,r:int,n:str,a:int,s:str):
    #     self.roll_no = r 
    #     self.name = n
    #     self.age = a
    #     self.standard = s

    def display(self): #current instance of the class.instance mean object 
        print(
            f"Roll no = {self.roll_no}, Name = {self.name} , Age = {self.age}, Standard = {self.standard} , school = {self.school}"
        )


s1  = Student(1,"javeed",13,12)
#s1.set_information(1,"shashi",18,8)


# s1.age =5
# s1.name="shashi"
# s1.standard = "gold"
# print(s1.roll_no)
# print(s1.name)
# print(s1.standard)
# print(s1.age)

s1.display()
