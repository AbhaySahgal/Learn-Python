#A lambda function is a small one‑line function without a name.
#Structure of Lambda - 
#lambda arguments : expression

#Normal Function -
def square(x):

    return x * x

print(square(5))


#Same Function using Lambda

square = lambda x: x*x
print(square(5))



#Lambda with map()
#map() applies a function to every item in a list.

nums = [1,2,3,4]
result = list(map(lambda x: x*2, nums))
print(result)





#Lambda with filter()
#filter() selects items based on a condition.

nums = [1,2,3,4,5,6]
even = list(filter(lambda x: x%2 == 0, nums))
print(even)





#Lambda in Sorting (Very Common)

students = [
    ("Abhay",90),
    ("Rahul",70),
    ("Neha",85)
]

students.sort(key=lambda x: x[1])

print(students)