#try --> Risky code
#except -> handle error
#finally -> always runs

# Write program that:

# 1️⃣ asks user for number
# 2️⃣ prints square
# 3️⃣ handles invalid input

# try:
#     num = int(input("Enter number: "))
#     square = num*num
#     print(f"Square of number is: {square}")
# except:
#     print("Invalid Type")







# Write program that:

# 1️⃣ asks user for number
# 2️⃣ prints:

# 100 / number

# Handle:

# division by zero
# invalid input

# try:
#     num = int(input("Enter number: "))
#     dzero = 100/ num
#     print(f"Result is: {dzero}")
# except ValueError:
#     print("Invalid Type")

# except ZeroDivisionError:
#     print("Can not divide by Zero")






#Safe Calculator

try:
    num1 = int(input("\nEnter first number: "))
    opr = input("\nEnter operator(+ - * /): ")
    num2 =  int(input("\nEnter Second number: "))
    
    if opr == "+":
        print(num1 + num2)
    elif opr == "-":
        print(num1 - num2)
    elif opr == "*":
        print(num1 * num2)
    elif opr == "/":
        print(num1 / num2)
    else:
        print("Invalid Operator")


except ZeroDivisionError:
    print("Error: Can not divide by Zero")