class Flight:
    hour = 10
    date = "21/07/2020"
    def get_hour(self):
        return self.hour
    def get_date(self):
        return self.date
    def print_object(self):
        print(self.get_date())
        print(self.get_hour())

flight1 = Flight()
flight1.print_object()

#constructors
class Student:
    name = ""
    cod = 0
    def __init__(self, name, cod):
        self.name = name
        self.cod = cod
    def print_object(self):
        print(self.cod)
        print(self.name)

student1 = Student(name="Rodrigo", cod=12345)
student1.print_object()

#inheritance

class Animal:
    def walk(self):
        print("waling")

class Dog(Animal):
    pass

dog1 = Dog()
dog1.walk()