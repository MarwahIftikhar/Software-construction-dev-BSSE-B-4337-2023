# 1. Car class
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

# Example usage
my_car = Car("Toyota", "Red")
print("Model:", my_car.model)
print("Color:", my_car.color)

# 2. Rectangle area and perimeter
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Example usage
rect = Rectangle(5, 3)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())

# 3. Student class with average
class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.marks = [m1, m2, m3]

    def average(self):
        return sum(self.marks)/3

# Example usage
s = Student("Ali", 80, 70, 90)
print("Average marks:", s.average())

# 4. Check pass/fail
class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.marks = [m1, m2, m3]

    def passed(self):
        if min(self.marks) >= 40:
            return "Passed"
        else:
            return "Failed"

# Example usage
# s = Student("Sara", 50, 60, 30)
print(s.name, s.passed())

# 5 & 6. Account class with debit, credit, balance
class Account:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def credit(self, amount):
        self.balance += amount

    def print_balance(self):
        print("Balance:", self.balance)

# Example usage
a = Account(1234, 5000)
a.credit(1000)
a.debit(2000)
a.print_balance()

# 7 & 8. Employee class with annual salary
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

# Example usage
e = Employee(1, "Ali", 5000)
print("Annual salary:", e.annual_salary())

# 9. Bank Account class with private balance
class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.__balance = balance   # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

# Example usage
b = BankAccount(1001, 5000)
b.deposit(1000)
b.withdraw(2000)
print("Balance:", b.get_balance())

# 10. Student class with private name and marks
class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def display(self):
        print("Name:", self.__name)
        print("Marks:", self.__marks)

# Example usage
s = Student("Sara", [80, 70, 90])
s.display()

# 11. Employee class with private salary
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def update_salary(self, new_salary):
        self.__salary = new_salary

    def display_salary(self):
        print("Salary of", self.name, "is", self.__salary)

# Example usage
e = Employee("Ali", 5000)
e.display_salary()
e.update_salary(6000)
e.display_salary()





# 1. Vehicle and Car (Single Inheritance)
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

# Example usage
c = Car("Toyota", "Corolla")
c.display()

# 2. Person and Student (Single Inheritance)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def display(self):
        print("Student Name:", self.name)
        print("Age:", self.age)

# Example usage
s = Student("Ali", 20)
s.display()

# 3. Grandparent → Parent → Child (Multilevel Inheritance)
class Grandparent:
    def __init__(self, g_name):
        self.g_name = g_name

class Parent(Grandparent):
    def __init__(self, g_name, p_name):
        super().__init__(g_name)
        self.p_name = p_name

class Child(Parent):
    def __init__(self, g_name, p_name, c_name):
        super().__init__(g_name, p_name)
        self.c_name = c_name

    def display(self):
        print("Grandparent:", self.g_name)
        print("Parent:", self.p_name)
        print("Child:", self.c_name)

# Example usage
f = Child("Ahmed", "Bilal", "Sara")
f.display()

# 4. Device → Computer → Laptop (Multilevel Inheritance)
class Device:
    def __init__(self, brand):
        self.brand = brand

class Computer(Device):
    pass

class Laptop(Computer):
    def display(self):
        print("Laptop Brand:", self.brand)

# Example usage
l = Laptop("Dell")
l.display()

# 5. Person → Employee → Manager (Multilevel Inheritance)
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    pass

class Manager(Employee):
    def display(self):
        print("Manager Name:", self.name)

# Example usage
m = Manager("Sara")
m.display()

# 6. Academics + Sports → Student (Multiple Inheritance)
class Academics:
    def __init__(self, subject):
        self.subject = subject

class Sports:
    def __init__(self, sport):
        self.sport = sport

class Student(Academics, Sports):
    def __init__(self, subject, sport):
        Academics.__init__(self, subject)
        Sports.__init__(self, sport)

    def display(self):
        print("Subject:", self.subject)
        print("Sport:", self.sport)

# Example usage
s = Student("Math", "Cricket")
s.display()

# 7. Camera + Music Player → Smartphone (Multiple Inheritance)
class Camera:
    def __init__(self, camera_feature):
        self.camera_feature = camera_feature

class MusicPlayer:
    def __init__(self, music_feature):
        self.music_feature = music_feature

class Smartphone(Camera, MusicPlayer):
    def __init__(self, camera_feature, music_feature):
        Camera.__init__(self, camera_feature)
        MusicPlayer.__init__(self, music_feature)

    def display(self):
        print("Camera Feature:", self.camera_feature)
        print("Music Feature:", self.music_feature)

# Example usage
phone = Smartphone("12MP Camera", "MP3 Player")
phone.display()
