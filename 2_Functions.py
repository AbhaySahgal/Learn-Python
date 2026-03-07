#Functions help you reuse code

#syntax: 
# def function_name():
#     code


#Defining a Function
def greet(): 
    print("Hello Abhay")

greet() #function calling


#Function with Parameter

def greet(name):
    print("Hello", name)

greet("Abhay")

#Return Statement - program beacome modular and reusable
def add(a, b):
    return a+b
result = add(5, 3)
print(result)


#Create a Calculator using Functions

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

def add(a, b):
    return a+b

def substract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a / b

result = print("Addition:", add(a,b))
result = print("Substraction:", substract(a,b))
result = print("Multiplication:", multiply(a,b))
result = print("Division:", divide(a,b))


#NOTE
#return is used to send a value back from a function to a place where the function was called.



