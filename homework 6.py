#0
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f'Person({self.first_name}, {self.last_name}, {self.age})'

# Instantiate an object of the Person class
person = Person('John', 'Smith', 25)

# Print the object
print(person)

#1
class Email:
    def __init__(self, address):
        self.address = address

    def __eq__(self, other):
        if isinstance(other, Email):
            return self.address.lower() == other.address.lower()
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

# Testing the equality and inequality operators
email1 = Email("example@example.com")
email2 = Email("Example@Example.com")
email3 = Email("test@test.com")

print(email1 == email2)  # True, because the addresses are the same (case-insensitive)
print(email1 != email2)  # False, because the addresses are the same (case-insensitive)
print(email1 == email3)  # False, because the addresses are different
print(email1 != email3)  # True, because the addresses are different

#2
class Student:
    def __init__(self, name, age):
        self._name = name  # Protected attribute
        self._age = age    # Protected attribute

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, value):
        self._name = value

    # Getter for age
    @property
    def age(self):
        return self._age

    # Setter for age
    @age.setter
    def age(self, value):
        if value >= 0:  # Simple validation to ensure age is non-negative
            self._age = value
        else:
            raise ValueError("Age cannot be negative")

# Demonstration of usage
student = Student("Alice", 20)

# Accessing protected attributes via getters
print(student.name)  # Output: Alice
print(student.age)   # Output: 20

# Modifying protected attributes via setters
student.name = "Bob"
student.age = 25

print(student.name)  # Output: Bob
print(student.age)   # Output: 25

# Attempting to set a negative age will raise an error
try:
    student.age = -5
except ValueError as e:
    print(e)  # Output: Age cannot be negative

#3
class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance

# Demonstration of the BankAccount class
account = BankAccount(100)  # Initial balance of $100
print(f"Initial Balance: ${account.get_balance()}")

account.deposit(50)
print(f"Balance after deposit: ${account.get_balance()}")

account.withdraw(30)
print(f"Balance after withdrawal: ${account.get_balance()}")

account.withdraw(150)  # Attempt to withdraw more than the balance
print(f"Final Balance: ${account.get_balance()}")

#4
class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area() and self.perimeter() == other.perimeter()
        return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            if self.area() == other.area():
                return self.perimeter() < other.perimeter()
            return self.area() < other.area()
        return False

# Test the comparison operators with multiple instances
rect1 = Rectangle(4, 5)
rect2 = Rectangle(2, 10)


print(f"Rectangle 1: Length = {rect1.length}, Width = {rect1.width}, Area = {rect1.area()}, Perimeter = {rect1.perimeter()}")
print(f"Rectangle 2: Length = {rect2.length}, Width = {rect2.width}, Area = {rect2.area()}, Perimeter = {rect2.perimeter()}")


print(f"Rectangle 1 == Rectangle 2: {rect1 == rect2}")
print(f"Rectangle 1 < Rectangle 2: {rect1 < rect2}")

#5
from abc import ABC, abstractmethod

# Abstract class Vehicle
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

# Subclass Car
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")

# Subclass Bicycle
class Bicycle(Vehicle):
    def start_engine(self):
        print("Bicycles don't have engines, but let's start pedaling!")

# Demonstrating polymorphism
def start_vehicle_engine(vehicle):
    vehicle.start_engine()

# Creating instances of Car and Bicycle
car = Car()
bicycle = Bicycle()

# Calling the start_engine method on both instances
start_vehicle_engine(car)      # Output: Car engine started.
start_vehicle_engine(bicycle)  # Output: Bicycles don't have engines, but let's start pedaling!

#6
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __len__(self):
        return self.pages

# Creating instances of the Book class
book1 = Book("1984", "George Orwell", 328)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)

# Demonstrating the use of __str__ and __len__ methods
print(str(book1))  # Output: '1984' by George Orwell
print(len(book1))  # Output: 328

print(str(book2))  # Output: 'To Kill a Mockingbird' by Harper Lee
print(len(book2))  # Output: 281

#7
class Animal:
    def __init__(self, species):
        self.species = species

    def __str__(self):
        return f"This is a {self.species}."

class Dog(Animal):
    def __init__(self):
        super().__init__("Dog")

    def __str__(self):
        return f"This is a {self.species}. Woof!"

class Cat(Animal):
    def __init__(self):
        super().__init__("Cat")

    def __str__(self):
        return f"This is a {self.species}. Meow!"

# Polymorphism in action
animals = [Dog(), Cat()]

for animal in animals:
    print(animal)

#8
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for salary
    def get_salary(self):
        return self.__salary

    # Setter for salary
    def set_salary(self, salary):
        self.__salary = salary

    def display_employee(self):
        print(f"Name: {self.__name}, Salary: {self.__salary}")


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.__department = department

    # Getter for department
    def get_department(self):
        return self.__department

    # Setter for department
    def set_department(self, department):
        self.__department = department

    def display_manager(self):
        print(f"Name: {self.get_name()}, Salary: {self.get_salary()}, Department: {self.__department}")


# Example usage
emp = Employee("John Doe", 50000)
emp.display_employee()

mgr = Manager("Jane Smith", 75000, "HR")
mgr.display_manager()

#9
from datetime import datetime

class Employee:
    def __init__(self, name, start_date, PIN, phone, address, manager_name, department):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.PIN = PIN
        self.phone = phone
        self.address = address
        self.manager_name = manager_name
        self.department = department

    def calculate_tenure(self):
        today = datetime.today()
        tenure = today - self.start_date
        return tenure.days // 365  # Returns tenure in years

    def business_card(self):
        return (f"Name: {self.name}\n"
                f"Phone: {self.phone}\n"
                f"Address: {self.address}\n"
                f"Manager: {self.manager_name}\n"
                f"Department: {self.department}")

# Example usage:
employee = Employee("John Doe", "2015-06-01", "1234", "555-1234", "123 Main St", "Jane Smith", "Engineering")
print(f"Tenure: {employee.calculate_tenure()} years")
print("Business Card Info:")
print(employee.business_card())

#10
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
        self._messages = []

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    @abstractmethod
    def send_message(self, message):
        pass

    def get_messages(self):
        return self._messages

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self._department = department

    @property
    def department(self):
        return self._department

    def send_message(self, message):
        self._messages.append(message)
        print(f"Message to {self._name} (Manager of {self._department}): {message}")

class Team:
    def __init__(self, manager, members):
        self.manager = manager
        self.members = members

    def send_message_to_all(self, message):
        self.manager.send_message(message)
        for member in self.members:
            member.send_message(message)

# Example usage
manager = Manager("Alice", 90000, "Engineering")
employee1 = Manager("Bob", 50000, "Sales")  # Example of another manager as a team member
employee2 = Manager("Charlie", 60000, "Marketing")  # Example of another manager as a team member

team = Team(manager, [employee1, employee2])
team.send_message_to_all("Team meeting at 10 AM tomorrow.")
