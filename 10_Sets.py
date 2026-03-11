#Sets are a data structure used to store unique values.
#set() automatically removes duplicates
# Sets do not keep order.

numbers = {1,2,3,4}
print(numbers)





#Removing Duplicates(Most common use)
nums = [1,2,2,3,4,4,5]
unique_nums = set(nums)
print(unique_nums)





#Adding Elements to a Set
s = {1,2,3}
s.add(4)
print(s)
s.remove(3)
print(s)

numbers = {5,10,15}

for n in numbers:
    print(n)








#SET OPERATION
#Union(combine sets)

a = {1,2,3}
b= {3,4,5}

print(a | b)

#Intersection
print(a & b)

#Difference
print(a - b)










#Task-1

print("\nTask-1")

nums = [5,5,6,7,7,8,9]

exp = set(nums)

print(exp)







#Task-2
print("\nTask-2")

list1 = [1,2,3,4]
list2 = [3,4,5,6]

exp = set(list1) & set(list2)

print(exp)









#Unique Word Finder
print("\nUnique Word Finder")


sentence = "Python is fun and python is powerful"

unq = set(sentence.split())

print(unq)

