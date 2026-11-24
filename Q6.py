class Camera:
    def take_photo(self):
        print("Taking photo")

class Phone:
    def make_call(self):
        print("Making a call")

class SmartPhone(Camera, Phone):
    def browse(self):
        print("Browsing internet")

s = SmartPhone()
s.take_photo()
s.make_call()
s.browse()