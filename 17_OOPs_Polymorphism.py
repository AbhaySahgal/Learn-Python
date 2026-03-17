#Polymorphism = poly + morphism
#poly --> many
#morphism --> forms

#Same function/Method can behave differently depending on object.

# One action --> different result

#Example -->

class Animal:

    def sound(self):
        print("Animals makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

a = Animal()
d = Dog()
c = Cat()

a.sound()
d.sound()
c.sound()