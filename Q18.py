class Camera:
    def take_photo(self):
        print("Photo captured")

class MusicPlayer:
    def play_music(self):
        print("Playing music")

class SmartPhone(Camera, MusicPlayer):
    def make_call(self):
        print("Making a call")

s = SmartPhone()
s.take_photo()
s.play_music()
s.make_call()