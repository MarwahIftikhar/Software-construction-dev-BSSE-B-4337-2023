r = float(input("Enter radius: "))
area = 3.14 * r * r
print("Area of circle:", area)



a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

temp = a
a = b
b = temp

print("After swap:")
print("a =", a)
print("b =", b)



#fahrenheit
c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print("Temperature in Fahrenheit:", f)

# Total Marks and Percentage (5 Subjects)

m1 = int(input("Enter marks 1: "))
m2 = int(input("Enter marks 2: "))
m3 = int(input("Enter marks 3: "))
m4 = int(input("Enter marks 4: "))
m5 = int(input("Enter marks 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = (total / 500) * 100

print("Total Marks:", total)
print("Percentage:", percentage)


# teger to Float & Float to Integer
a = int(input("Enter an integer: "))
b = float(input("Enter a float: "))

a_float = float(a)
b_int = int(b)

print("Integer to float:", a_float)
print("Float to integer:", b_int)

# 6. List: Sum, Max, Min
numbers = [10, 20, 30, 40, 50]

print("Sum:", sum(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))

# 7. Take 5 Names and Store in List
names = []

for i in range(5):
    name = input("Enter name: ")
    names.append(name)

print(names)

# 8. Add Element using append()
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

# 9. Insert Element at Specific Index
my_list = [10, 20, 30]
my_list.insert(1, 15)
print(my_list)

# 10. Remove Element using remove() and pop()
my_list = [5, 10, 15, 20]

my_list.remove(10)
print("After remove:", my_list)

my_list.pop()
print("After pop:", my_list)

# 11. Tuple with 10 Elements
my_tuple = (1, 2.5, "A", 4, 5.5, "Hello", 7, 8.8, "Python", 10)
print(my_tuple)

# 12. Count Element in Tuple
t = (1, 2, 3, 2, 2, 4)
print(t.count(2))

# 13. Tuple → List → Modify → Tuple
t = (1, 2, 3)
l = list(t)

l.append(4)

t = tuple(l)
print(t)

# 14. Nested Tuple Access
nested = (1, 2, (3, 4, 5))
print(nested[2][1])

# 15. Set with 7 Elements
my_set = {1, 2.5, "A", 4, "B", 6, 7.7}
print(my_set)

# 16. Add & Update Set
my_set = {1, 2, 3}

my_set.add(4)
my_set.update([5, 6, 7])

print(my_set)

# 17. Remove & Discard from Set
my_set = {10, 20, 30}

my_set.remove(20)
my_set.discard(40)

print(my_set)

# 18. Union of Two Sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))

# 19. Intersection of Two Sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.intersection(set2))



