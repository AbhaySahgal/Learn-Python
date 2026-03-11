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





