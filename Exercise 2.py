# Exercise 1: Create the Person Class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.get_age()}")
    def get_age(self):
        return self.__age

person1 = Person("Lina", 20)
person1.display_info()

# Reflection: It is because it can keep the attributes you want to be private to become private