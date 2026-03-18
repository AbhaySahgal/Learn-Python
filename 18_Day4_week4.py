# Class Variables vs Instance Variables + Static Method

#Instance Variable - These variables are different for every object

#Example - 

# class Student:

#     def __init__(self, name, marks):
#         self.name = name    #instance variable
#         self.marks = marks  #instance variable

# s1 = Student("Abhay", 90)
# s2 = Student("Rahul", 85)

# print(s1.name, s1.marks)
# print(s2.name, s2.marks)

#Each object has its own data





# Class variable - these variable are shared by all objects

#Example -

# class Student:

#     school = "ABC School"

#     def __init__(self, name):
#         self.name = name

# s1 = Student("Abhay")
# s2 = Student("Mukesh")

# print(s1.school)
# print(s2.school)

#Same school for every student




# Static Method - (utility function is classes) - Static method does not use object

#Example -

# class Mathutils:

#     @staticmethod
#     def add(a, b):
#         return a + b
    
# print(Mathutils.add(2,3))

#No self
#call using class name


