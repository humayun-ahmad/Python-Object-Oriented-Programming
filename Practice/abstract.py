from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass
    

# car = Vehicle()

class Car(Vehicle):

    def go(self):
        print("Car is going")


    def stop(self):
        print("Car stopped")

# car = Car()

# car.go()
# car.stop()

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("You stop motorcycle")
    
motorcycle = Motorcycle()

motorcycle.go()
motorcycle.stop()

class Boat(Vehicle):
    def go(self):
        print("You ride the boart")

    def stop(self):
        print("You stop boat")
    
boat = Boat()

boat.go()
boat.stop()


