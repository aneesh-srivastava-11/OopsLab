class Shape:
    def area(self):
        pass

class Square(Shape):
    def area(self):
        return 5 * 5

class Circle(Shape):
    def area(self):
        return 3.14 * 4 * 4

for s in (Square(), Circle()):
    print(s.area())
