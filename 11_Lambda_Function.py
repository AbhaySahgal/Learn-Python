#A lambda function is a small one‑line function without a name.
#Structure of Lambda - 
#lambda arguments : expression

#Normal Function -
# def square(x):

#     return x * x

# print(square(5))


#Same Function using Lambda

# square = lambda x: x*x
# print(square(5))



#Lambda with map()
#map() applies a function to every item in a list.

# nums = [1,2,3,4]
# result = list(map(lambda x: x*2, nums))
# print(result)





#Lambda with filter()
#filter() selects items based on a condition.

# nums = [1,2,3,4,5,6]
# even = list(filter(lambda x: x%2 == 0, nums))
# print(even)





#Lambda in Sorting (Very Common)

# students = [
#     ("Abhay",90),
#     ("Rahul",70),
#     ("Neha",85)
# ]

# students.sort(key=lambda x: x[1])

# print(students)












#Task-1 
# print("\nTask-1")

# num = int(input("Enter the number: "))
# mul = lambda x: x * 10
# print("Multiple of 10 of that number is: ", mul(num))







#Task-2
# print("Task-2")

# nums = [5,12,8,20,3]

# greater = list(filter(lambda x: x>10, nums))

# print("Greater than 10 in the list: ", greater)











#Student Score Sorter

students = [
    ("Abhay",88),
    ("Rahul",72),
    ("Neha",95),
    ("Aman",80)
]

sorted = students.sort(key = lambda x: x[1], reverse= True)
print("Sorted list is: ", students)









