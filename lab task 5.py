# Final price after tax
def final_price(price, tax_percent):
    tax_amount = price * tax_percent / 100
    return price + tax_amount

# Example usage
p = float(input("Enter price: "))
t = float(input("Enter tax percentage: "))
print("Final price:", final_price(p, t))

# 2. Factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Example usage
num = int(input("Enter a number: "))
print("Factorial:", factorial(num))
# Temperature classification
def temp_classification(temp):
    if temp < 10:
        return "Cold"
    elif temp <= 25:
        return "Warm"
    else:
        return "Hot"

# Example usage
c = float(input("Enter temperature in Celsius: "))
print("Temperature is", temp_classification(c))

# 4. Sum, Difference, Product of two numbers
def operations(a, b):
    s = a + b
    d = a - b
    p = a * b
    return s, d, p

# Example usage
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

sum_, diff, prod = operations(x, y)
print("Sum:", sum_)
print("Difference:", diff)
print("Product:", prod)

# Sum of values in a list
def sum_list(lst):
    total = 0
    for item in lst:
        total += item
    return total

# Example usage
numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
print("Sum of list:", sum_list(numbers))