class Mobile:
    def call(self):
        print("Making a call")

class Smartphone(Mobile):
    def camera(self):
        print("Taking a photo")

s = Smartphone()
s.call()
s.camera()