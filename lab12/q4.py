class Laptop:
    def code(self):
        print("Coding Python...")

class Mobile:
    def code(self):
        print("Coding in Notes app...")

def developer(device):
    device.code()

developer(Laptop())
developer(Mobile())
