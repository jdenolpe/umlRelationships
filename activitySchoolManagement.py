# Exercise 1: Create the Person Class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}\nAge: {self.age}")

person1 = Person("Lina", 20)
person1.display_info()