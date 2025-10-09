#write program to demonstrate constructor overloading
class Overloading:
  def __init__(self,name):
    self.name=name
  def __init__(self,name,age):
    self.name=name
    self.age=age
obj7=Overloading('Aneesh')

obj8=Overloading('kushagra',19)