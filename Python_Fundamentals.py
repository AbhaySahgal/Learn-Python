#Basic printing in python

# print("Hello, World!")
# print("My name is Abhay")
# print("I am learning Python")
# print("This is my first program")

#Variables in python

# name = "Abhay"
# age = 25

# print(name)
# print(age)

#exercise

# Write a program that prints:

# My name is Abhay
# I am learning Python
# I will become a Python developer





# name = "Abhay"
# lang = "Python"
# role = "Python developer"

# print("My name is", name)
# print("I am learning", lang)
# print("I will become a", role)





#Input in Python

# name = input("Enter your Name:")
# print("Hello,", name) #input always return string

# age = input("Enter your Age:")
# print(type(age))





#For use as Int or other the string we can typeconversion

# age = int(input("Enter your age:" ))
# print(type(age))




# num1 = int(input("Enter first Number:" ))
# num2 = int(input("Enter second Number:" ))

# Addition = num1 + num2
# Substraction = num1 - num2
# Multiplication = num1 * num2
# Division = num1 / num2
# Modulas = num1 % num2
# Power = num1 ** num2
# Floor_Division = num1 // num2

# print(Addition , Substraction , Multiplication , Division, Modulas, Power, Floor_Division)





# Check if number is odd or even

# num = int(input("Enter number: "))

# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")




#Comparison Operator

# | Operator | Meaning          | Example |
# | -------- | ---------------- | ------- |
# | ==       | equal            | x == y  |
# | !=       | not equal        | x != y  |
# | >        | greater than     | x > y   |
# | <        | less than        | x < y   |
# | >=       | greater or equal | x >= y  |
# | <=       | less or equal    | x <= y  |

#elif 

# marks = int(input("Enter marks: "))

# if marks >= 90:
#     print("Grade A")

# elif marks >= 75:
#     print("Grade B")

# elif marks>= 50:
#     print("Grade C")

# else:
#     print("Fail")


#Login System

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "python123":
    print("Login Successful")

else:
    print("Invalid credentials")