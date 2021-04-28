cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)

cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")
print(cars)

class Person:
  def __init__(self, name,lastname, age):
    self.name = name
    self.lastname = lastname
    self.age = age

p1 = Person("John", "Walker", 40)

print(p1.name)
print(p1.lastname)
print(p1.age)


class Person:
  def __init__(self, name, lastname, age):
    self.name = name
    self.lastname = lastname
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name+  " " +self.lastname)

p1 = Person("John", "Walker", 36)
p1.myfunc()