#Recap of list comprehension

nums = [1,2,3,4]

squares =[]
for n in nums:
    squares.append(n*n)

print(squares)

#now more shorter and cleaner version of List Comprehension

nums = [5,6,7,8]
squares = [n*n for n in nums]
print(squares)

