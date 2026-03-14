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

#List Comprehension with Condition

nums = [1,2,3,4,5,6]
evens = [n for n in nums if n % 2 == 0]
print(evens)

#Dictionary Comprehension

nums = [1,2,3,4]
squares = {n: n*n for n in nums}
print(squares)



#Task-1
print("Task-1")

nums = [1,2,3,4]
mul = [n*10 for n in nums]
print(mul)


#Task-2
print("Task-2")

numbers = [2,3,4]
squares = {n: n**2 for n in numbers}
print(squares)

#Word Frequency Counter
from collections import Counter

sentence = "python is easy and python is powerful"

words = sentence.split()
freq = {}
for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

print(freq)

