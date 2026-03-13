
#Advanced Strings

#user input
#file data
#APIs
#web Dev
#automation scripts


#Strip - Cleaning user input - strip() - removes spaces from start and end

#lower() and upper() - coverts text cases

#split() - Breaks Text into Words

#join() - Combine Words

#replace() - replace part of string


name = "    Abhay   "
print(name.strip())

text = "Python"

print(text.lower())
print(text.upper())

#use case- 
# user = input("Enter yes/no: ")

# if user.lower() == "yes":
#     print("Confirmed")


words = ["python","is","fun"]
sentence = " ".join(words)
print(sentence)




