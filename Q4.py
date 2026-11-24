class Grandfather:
    def grandfather_property(self):
        print("Grandfather owns a house")

class Father(Grandfather):
    def father_property(self):
        print("Father owns a car")

class Son(Father):
    def son_property(self):
        print("Son owns a bike")

s = Son()
s.grandfather_property()
s.father_property()
s.son_property()