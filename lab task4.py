# Squares of numbers 1–10
for i in range(1, 11):
    print("Square of", i, "is", i*i)

# Count vowels in a string
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)

# Marks greater than 50
marks = [45, 67, 32, 89, 54]

for mark in marks:
    if mark > 50:
        print(mark)

# Multiplication table
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num*i)

# Odd numbers 1–20 using while loop
i = 1
while i <= 20:
    if i % 2 != 0:
        print(i)
    i += 1

# Repeat asking password
correct = "1234"
password = ""

while password != correct:
    password = input("Enter password: ")

print("Password correct!")

# Keep input until “stop”
text = ""
while text.lower() != "stop":
    text = input("Type something (or stop to end): ")

# Sum of numbers 1 to n
n = int(input("Enter n: "))
total = 0

for i in range(1, n+1):
    total += i

print("Sum:", total)

# Largest number in list (without max)
numbers = [10, 45, 32, 67, 21]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is", largest)

# Print all elements of a list
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

# Read numbers until negative, then print average
total = 0
count = 0

while True:
    num = int(input("Enter number: "))
    if num < 0:
        break
    total += num
    count += 1

if count != 0:
    print("Average is", total / count)
else:
    print("No numbers entered")

# Check palindrome using while loop
num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if reverse == original:
    print("Palindrome")
else:
    print("Not palindrome")