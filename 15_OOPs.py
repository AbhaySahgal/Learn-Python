#OOPs means organising code using Classes and Objects.

# Class = blueprint
# Object = real thing created from blueprint

# class Student:
#     name = "Abhay"
#     marks = 90

# s1 = Student()


# print(s1.name)
# print(s1.marks)


# class Students: --> Creating class
# name, marks --> varibles inside class
# s1 = Student() -> Oject creation
# s1.name --> access data



# Constructor(__init__) --> used to initilize object data

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

# s1 = Student("Abhay", 90)

# print(s1.name)
# print(s1.marks)


# __init__ runs automatically
# self means current object


#Methods(Functions inside class)

# class Student:
#     def __int__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     def show(self):
#         print(self.name, self.marks)

# s1 = Student("Abhay", 90)
# s1.show()


#Practice Task

# class Car():
#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed
    
#     def show(self):
#         print(self.brand, self.speed)

# s1 = Car("BMW", 300)
# s2 = Car("Audi", 400)

# s1.show()
# s2.show()



#Mini Project --> Student Result System

#class should take name, marks, and method -> print Pass/Fail

# class Result:

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def show(self):
#         if self.marks >= 40:
#             print(self.name, ": Pass")
#         else:
#             print(self.name, ": Fail")


# s1 = Result("Abhay", 90)
# s2 = Result("Mukesh", 39)

# s1.show()
# s2.show()




#Task-2

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()

        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "Fail"

    def show(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Average:", self.average())
        print("Grade:", self.grade())
        print()


s1 = Student("Abhay", [80, 90, 70])
s2 = Student("Rahul", [50, 60, 55])

s1.show()
s2.show()