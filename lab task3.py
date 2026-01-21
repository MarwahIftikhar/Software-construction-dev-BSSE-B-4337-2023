# Dictionary of 3 students
students = {"Ali": 80, "Sara": 90, "Ahmed": 75}

for name in students:
    print(name, ":", students[name])

#  Add new key-value pair
students = {"Ali": 80, "Sara": 90}
students["Ayesha"] = 85
print(students)

#  Access a value by key
students = {"Ali": 80, "Sara": 90}
print("Sara's marks:", students["Sara"])

#  Update an existing value
students = {"Ali": 80, "Sara": 90}
students["Ali"] = 95
print(students)

#  Remove key-value using pop() and del
students = {"Ali": 80, "Sara": 90, "Ahmed": 75}

students.pop("Sara")
print(students)

del students["Ahmed"]
print(students)

# Merge two dictionaries
dict1 = {"Ali": 80, "Sara": 90}
dict2 = {"Ahmed": 75, "Ayesha": 85}

dict1.update(dict2)
print(dict1)

# Check positive, negative, or zero
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Largest of 3 numbers
a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))

if a > b and a > c:
    print("Largest is", a)
elif b > c:
    print("Largest is", b)
else:
    print("Largest is", c)

# Calculate discount
total = float(input("Enter total amount: "))

if total >= 500:
    discount = total * 0.2
elif total >= 200:
    discount = total * 0.1
else:
    discount = 0

final_price = total - discount
print("Discount:", discount)
print("Final price:", final_price)

# Username and password check
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Login failed")

# Password strength
password = input("Enter password: ")

if len(password) < 6:
    print("Weak")
elif len(password) < 10:
    print("Medium")
else:
    print("Strong")

# Speed fine
speed = int(input("Enter speed: "))

if speed <= 60:
    print("No fine")
elif speed <= 80:
    print("Small fine")
else:
    print("Heavy fine")

# Shop discount
price = float(input("Enter total price: "))

if price >= 1000:
    discount = price * 0.2
elif price >= 500:
    discount = price * 0.1
else:
    discount = 0

final_price = price - discount
print("Discount:", discount)
print("Final price:", final_price)

# Weather classification
temp = float(input("Enter temperature: "))
humidity = float(input("Enter humidity: "))
wind = float(input("Enter wind speed: "))

if temp < 30 and humidity < 50 and wind < 20:
    print("Pleasant")
elif temp < 40 and humidity < 70:
    print("Normal")
else:
    print("Harsh")
