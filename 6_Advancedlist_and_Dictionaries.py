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
# students = [
#     {"name": "Abhay","marks": 92},
#     {"name": "Rahul", "marks": 85},
#     {"name": "Neha", "marks": 88}
# ]

# for s in students:
#     print(s["name"], s["marks"])




#Task-1

# marks = [78, 90, 85, 66, 92]

# print(max(marks))
# print(min(marks))
# print(sum(marks))


#Task-2

# details = [
#     {"name": "abhay", "age": 22, "city": "Ayodhya"},
# ]

# for d in details:
#     print(d["name"], d["age"], d["city"])





#Student mark Analyser

students = [
    {"name" : "Abhay", "marks": 90},
    {"name" : "Rahul", "marks": 95},
    {"name" : "Neha", "marks": 85}
]

#Find top Student
top_student = students[0]

for s in students:
    if s["marks"] > top_student["marks"]:
        top_student = s

print("Topper Student: ", top_student["name"])

#Finding Avg Marks
total = 0
for s in students:
    total += s["marks"]

average = total/ len(students)
print("Average marks: ", average)

#Print All Student Names
print("All Students: ")

for s in students:
    print(s["name"])