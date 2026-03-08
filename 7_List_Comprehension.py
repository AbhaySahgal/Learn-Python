#this is most loved python features.
#It allows you to write loops in one line.


#Create a list of squares
#From normal loops

# numbers = [1, 2, 3, 4, 5]

# squares = []

# for n in numbers:
#     squares.append(n*n)

# print(squares)



#Same from List Comprehension

numbers = [1, 2, 3, 4, 5]
squares = [n*n for n in numbers]
print(squares)