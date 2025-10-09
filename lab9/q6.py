#write program to demonstrate constructor chaining or constructor overriding
class Vehicle:
  def __init__(self,engine):
    print('Inside Vehicle Constructor')
    self.engine=engine
class Car(Vehicle):
  def __init__(self,engine,max_speed):
    super().__init__(engine)
    print('Inside Car Constructor')
    self.max_speed=max_speed
class Electric_car(Car):
  def __init__(self, engine, max_speed,km_range):
    super().__init__(engine,max_speed)
    print('Inside electric car constructor')
    self.km_range=km_range
ev=Electric_car('1500cc',240,750)
print(f'Engine={ev.engine},Max Speed={ev.max_speed},km_range={ev.km_range}')
