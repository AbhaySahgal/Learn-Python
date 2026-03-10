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

# a = int(input("Enter Value of a: "))
# b = int(input("Enter Value of b: "))

# try:
#     def divide(a, b):
#         return a/b
# except ZeroDivisionError:
#     print("Can not Divide by 0")

# except ValueError:
#     print("Invalid value")


# print("Division of a and b is: ", divide(a,b))








# 4️⃣ Word Counter (File Handling)

# Given a file notes.txt.

# Program should print:

# Total words in file: 120

# Hint

# read()
# split() -> used to split Characters into words.
# len()

#Solution

# with open("notes.txt", "r") as file:
#     content = file.read()
#     words = content.split()
#     print("Total words in file: ", len(words))










# 5️⃣ Shopping List Manager

# Program should:

# ask user to enter 5 items

# store them in a list

# print items alphabetically

# Example output

# Shopping list:
# bread
# eggs
# milk
# rice
# tea

#Solution

# shoppinglist = []

# for i in range(5):
#     item =  input("Enter items: ")
#     shoppinglist.append(item)

# shoppinglist.sort()

# print("Shopping list: ")

# for item in shoppinglist:
#     print(item)












#Top Student Finder

# students = [
#  {"name":"Abhay","marks":90},
#  {"name":"Rahul","marks":70},
#  {"name":"Neha","marks":85}
# ]

# top_student = students[0]

# for s in students:
#     if s["marks"] > top_student["marks"]:
#         top_student = s
# print("Top student", top_student["name"])







#Error Safe input

# try:
#     number = int(input("Enter a number: "))
#     print("Number is: ", number)

# except ValueError:
#     print("Invalid Number")











#Number Frequency Counter

# numbers = [1,2,2,3,3,3,4]


# freq = {}

# for n in numbers:
#     if n in freq:
#         freq[n] += 1
#     else:
#         freq[n] = 1

# for key, value in freq.items():
#     print(key, "->", value)










#Function + List

# def square_list(numbers):
#     return [n*n for n in numbers]

# nums = [1,2,3,4]

# result  = square_list(nums)
# print(result)














#Student File Writer

# name = input("Enter name: ")
# age = input("Enter age: ")
# marks = input("Enter marks: ")

# with open("Students.txt", 'w') as file:
#     file.write(f"name: {name}\n") 
#     file.write(f"age: {age}\n") 
#     file.write(f"marks: {marks}\n")

# print("Student file created")













#Vowel Count

sentence = input("Enter Sentence: ")

vowels = "aeiou"
count = 0

for char in sentence:
    if char.lower() in vowels:
        count += 1

print("Vowels in sentence: ", count)
