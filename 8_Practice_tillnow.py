# So far you have learned:

# Week 1

# ✔ Variables
# ✔ Conditions
# ✔ Loops
# ✔ Lists
# ✔ Dictionaries
# ✔ Functions

# Week 2

# ✔ Modules
# ✔ File handling
# ✔ Error handling
# ✔ Advanced lists
# ✔ List comprehension


# 1️⃣ Even Numbers List

# Ask user for a number n.
# Create a list of all even numbers from 1 to n using list comprehension.

#Solution
# num = int(input("Enter number: "))

# evenlist = []

# for i in range(1, num+1):
#     if i % 2 == 0:
#         evenlist.append(i)

# print(evenlist)







# 2️⃣ Student Grade System

# Create a dictionary:

# students = {
#     "Abhay": 85,
#     "Rahul": 65,
#     "Neha": 92
# }

# Print grade:

# 90+  → A
# 75-89 → B
# 60-74 → C
# <60 → Fail

# Output example

# Abhay : B
# Rahul : C
# Neha : A

#Solution 

# students = {
#     "Abhay" : 85,
#     "Rahul" : 65,
#     "Neha" : 92,
# }

# # .items() returns key and value together

# for name, marks in students.items():
    
#     if marks >= 90:
#         grade = "A"

#     elif marks >= 75:
#         grade = "B"
    
#     elif marks >= 60:
#         grade = "C"
#     else:
#         grade = "Fail"

#     print(name, ":", grade)






# 3️⃣ Safe Division Function

# Create a function:

# def divide(a, b)

# Handle errors:

# division by zero

# invalid input

# Example

# Enter numbers: 10 0
# Error: cannot divide by zero

# Use try/except.

#Solution

a = int(input("Enter Value of a: "))
b = int(input("Enter Value of b: "))

try:
    def divide(a, b):
        return a/b
except ZeroDivisionError:
    print("Can not Divide by 0")

except ValueError:
    print("Invalid value")


print("Division of a and b is: ", divide(a,b))
