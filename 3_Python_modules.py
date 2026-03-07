#Python Modules

#A module is a python that contain code(function, variables, classes).

#Built-in modules

# | Module   | Use                     |
# | -------- | ----------------------- |
# | math     | mathematical operations |
# | random   | random numbers          |
# | datetime | date and time           |
# | os       | system operations       |
# | json     | working with APIs/data  |





#Generate Random number between 1-100

# import random
# num = random.randint(1, 100)

# print(num)




#Dice simulator
# import random

# dice = random.randint(1,6)

# print("Dice rolled:", dice)





#Guess the Number Game

import random

num = random.randint(1, 10)

guess = int(input("Guess the random Number (1-10): "))

if num == guess:
    print("Correct")
elif guess <= 5:
    print("Too low")
else:
    print("Too high")
print("Random number was:", num)
