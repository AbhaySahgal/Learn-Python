#OOP Concepts — Encapsulation & Inheritance (Very Important)

#Encapsulation -> Hiding internal data and controlling access

#Binding data + behavior tohgether and restricting uncontrolled access.

#Inhertance - code reuse + logical Hierarchy - Child class uses features of parent class


#Task-1

# class Mobile:

#     def __init__(self, price):
#         self.__price = price

#     def set_price(self, new_price):
#         self.set_price = new_price
    
#     def get_price(self):
#         return self.__price
    
# m1 = Mobile(2000)

# print("Price: ", m1.get_price())

# m1.set_price(2500)

# print("Updated price: ", m1.get_price())



#Task-2

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def show(self):
        print("name: ", self.name)
        print("Breed: ", self.breed)

m1 = Dog("Tommy", "labrador")
m1.show()