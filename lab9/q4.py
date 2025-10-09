#default value change of constructors
class OverloadingDefault:
  def __init__(self,name,age=19,classroom='lhc 206'):
    self.name=name
    self.age=age
    self.classroom=classroom
  def show(self):
    print(self.name,self.age,self.classroom)
obj5=OverloadingDefault('Sarthak')
obj5.show()
obj6=OverloadingDefault('Aneesh',20,'lhc 208')
obj6.show()