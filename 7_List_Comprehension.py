#this is most loved python features.
#It allows you to write loops in one line.


#List comprehension -> [x for x in list if x>5]


#Create a list of squares
#From normal loops

# numbers = [1, 2, 3, 4, 5]

# squares = []

# for n in numbers:
#     squares.append(n*n)

# print(squares)





#Same from List Comprehension

# numbers = [1, 2, 3, 4, 5]
# squares = [n*n for n in numbers]
# print(squares)





#Create a numbers divisible by 10

# number = [10, 15, 20, 25, 30]

# div = []

# for i in number:
#     if i%10 == 0:
#         div.append(i)
        
# print("Divisible by 10: ", div)





#World Length Analyzer

words = ["python", "developer", "ai", "code"]

leng = []

for i in words:
    leng.append(len(i))

print(leng)