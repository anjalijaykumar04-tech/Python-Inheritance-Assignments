class Vehicle:
    def start(self):
        print("Vehicle started")

class Bike(Vehicle):
    def show(self):
        print("This is a Bike")

class Car(Vehicle):
    def show(self):
        print("This is a Car")

class Bus(Vehicle):
    def show(self):
        print("This is a Bus")

b = Bike()
b.start()
b.show()

c = Car()
c.start()
c.show()

bus = Bus()
bus.start()
bus.show()