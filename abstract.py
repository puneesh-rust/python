#Abstract class : An abstract class is like a blueprint for other classes.

#It cannot be instantiated directly (you can’t create objects from it).

#It can have abstract methods (methods with no implementation — just definition) and normal methods (with implementation).

#Any class that inherits from it must implement its abstract methods.

#In Python, we use the abc (Abstract Base Class) module to create abstract classes.
from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def start(self):  # abstract method (no body)
        pass

    def info(self):  # normal method
        print(f"This is a vehicle made by {self.brand}")

# Child class (must implement start())
class Car(Vehicle):
    def start(self):
        print(f"{self.brand} car is starting...")

# Child class
class Bike(Vehicle):
    def start(self):
        print(f"{self.brand} bike is starting...")

# my_vehicle = Vehicle("Generic")  # ❌ ERROR: Can't create object of abstract class

my_car = Car("Tesla")
my_bike = Bike("Yamaha")

my_car.start()   # Tesla car is starting...
my_car.info()    # This is a vehicle made by Tesla

my_bike.start()  # Yamaha bike is starting...
my_bike.info()   # This is a vehicle made by Yamaha
