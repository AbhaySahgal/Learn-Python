numbers = [1, 2, 3] #its Listsm 

numbers = (1, 2, 3) # now this is tuples 
print(numbers)
print(numbers[1])

#List -> []
#Tuple -> ()

#Tuple is Immutable and Faster
#Tuples are used when data should not change - Coordinates, dates, RGB colors, database records


#Tuple Unpacking

point = (4,7)

x, y = point

print(x)
print(y)

name, age = ("Abhay", 25)

print(name)
print(age)










#Task 1

numbers = (5,10,15,20)

print(numbers)











#Task 2
person = ("Abhay", 25, "India")

print(person[0])
print(person[1])
print(person[2])










import math

point1 = (2, 3)
point2 = (5, 7)

x1, y1 = point1
x2, y2 = point2

val = math.sqrt(((x2-x1)**2 + (y2-y1)**2))

print("Distance btw", point1, "and", point2, "is: ", val)