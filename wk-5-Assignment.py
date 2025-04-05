# Assignment for Week 
# Design Your Own Class
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def info(self):
        return f"Smartphone: {self.brand} {self.model}, Price: ${self.price}"

# Inheritance example
class Smartwatch(Smartphone):
    def __init__(self, brand, model, price, battery_life):
        super().__init__(brand, model, price)
        self.battery_life = battery_life

    def info(self):
        return f"Smartwatch: {self.brand} {self.model}, Price: ${self.price}, Battery Life: {self.battery_life} hours"

# Testing the classes
phone = Smartphone("Samsung", "A15", 18499)  
watch = Smartwatch("Samsung", "Galaxy Watch 5", 4299, 48)

print(phone.info())
phone.call("0746384028")
print(watch.info())
watch.call("0746384028")
# This code defines a Smartphone class with methods to call and display information about the smartphone.
# It also defines a Smartwatch class that inherits from Smartphone and adds a battery life attribute.
# The code then creates instances of both classes and demonstrates their functionality.
# The Smartphone class has a method to call a number and display its information.
# The Smartwatch class inherits from Smartphone and adds a battery life attribute.
# It overrides the info method to include battery life in the output.
# The code creates instances of both classes and demonstrates their functionality.


# ACTIVITY: POLYMORPHISM CHALLENGE
# Activity 2: Polymorphism Challenge
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Testing polymorphism
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()

