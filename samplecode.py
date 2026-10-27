
from abc import ABC, abstractmethod


class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def bark(self):
        return f"{self.name} says Woof!"


class Payable(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class Payment(Payable):
    def pay(self, amount):
        return f"Payment of {amount} completed"


class Room:
    def __init__(self, name):
        self.name = name


class House:
    def __init__(self):
        self.rooms = [Room("Kitchen"), Room("Bedroom")]


class Book:
    def __init__(self, title):
        self.title = title


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)


class Order:
    def __init__(self, item):
        self.item = item


class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def place_order(self, order):
        self.orders.append(order)


class Document:
    def __init__(self, content):
        self.content = content


class Printer:
    def print_document(self, document):
        return document.content


def main():
    dog = Dog("Buddy")
    print("Inheritance:", dog.bark())

    payment = Payment()
    print("Realization:", payment.pay(500))

    house = House()
    print("Composition:", [room.name for room in house.rooms])

    book = Book("Python Basics")
    library = Library()
    library.add_book(book)
    print("Aggregation:", [book.title for book in library.books])

    customer = Customer("Alex")
    order = Order("Laptop")
    customer.place_order(order)
    print("Association:", customer.name, "ordered", customer.orders[0].item)

    document = Document("Hello World")
    printer = Printer()
    print("Dependency:", printer.print_document(document))


if __name__ == "__main__":
    main()
