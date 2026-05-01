from abc import ABC, abstractmethod 
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def speak(self):
        pass

    def whoami(self):
        print("i am a animal")

#concrete class
class Sparrow(Animal):
    def fly(self):
        print("sparrow is flying")
    def eat(self):
        print("Sparrow is eating")
    def speak(self):
        print("sparrow is speaking")

s= Sparrow()
s.eat()
s.speak()
