class Bird:
    def fly(self):
        print("Bird can fly")

class Parrot(Bird):
    def speak(self):
        print("Parrot can speak")

p = Parrot()
p.fly()
p.speak()