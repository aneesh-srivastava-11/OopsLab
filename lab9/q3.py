#write program for demostrating the parametrized  constuctor


class Parametrized:
  def __init__(self,name,age,salary):
    self.name=name
    self.age=age
    self.salary=salary
  def show(self):
    print(self.name,self.age,self.salary)

obj3=Parametrized('Aneesh',20,2000)
obj3.show()
obj4=Parametrized('Jha',25,2500)
obj4.show()
    