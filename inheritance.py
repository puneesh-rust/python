class Animal:
    def __init__(self , name):
        self.name = name 
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    pass
class Lion(Animal):
    pass
class Mouse(Animal):
    pass

dog = Dog("sheru")        
print(dog.name)

        