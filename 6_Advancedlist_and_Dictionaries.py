#Advanced Lists & Dictonaries

#access index with enumarate() -> gives index + value

# numbers = [10, 20, 30]

# for index, value in enumerate(numbers):
#     print(index, value)





#Finding Maximum Value
# numbers = [10, 25, 7, 99, 32]

# print(max(numbers))




#other useful functions

# | Function | Purpose         |
# | -------- | --------------- |
# | max()    | largest number  |
# | min()    | smallest number |
# | sum()    | total           |





#Dictionary List
students = [
    {"name": "Abhay","marks": 92},
    {"name": "Rahul", "marks": 85},
    {"name": "Neha", "marks": 88}
]

for s in students:
    print(s["name"], s["marks"])