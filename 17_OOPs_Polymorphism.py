#Polymorphism = poly + morphism
#poly --> many
#morphism --> forms

#Same function/Method can behave differently depending on object.

# One action --> different result

#Example -->

# class Animal:

#     def sound(self):
#         print("Animals makes sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog Barks")

# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")

# a = Animal()
# d = Dog()
# c = Cat()

# a.sound()
# d.sound()
# c.sound()


#Task-1
# class Shape:
#     def draw(self):
#         print("I can draw")
    
# class Circle(Shape):
#     def draw(self):
#         print("Drawing circle")

# class Square(Shape):
#     def draw(self):
#         print("Drawing Square")

# s = Shape()
# c = Circle()
# d = Square()

# s.draw()
# c.draw()
# d.draw()



#Task-2

# class Notification:
#     def send(self):
#         print("Sending Notification")

# class Email:
#     def send(self):
#         print("Sending Email")

# class Sms:
#     def send(self):
#         print("Sending Sms")

# n = Notification()
# e = Email()
# s = Sms()

# n.send()
# e.send()
# s.send()



#Task-3

# class Add:

#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def result(self):
#         print("Addition:", self.a + self.b)


# class Multiply:

#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def result(self):
#         print("Multiplication:", self.a * self.b)


# obj1 = Add(5, 3)
# obj2 = Multiply(5, 3)

# obj1.result()
# obj2.result()