
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


# name = "    Abhay   "
# print(name.strip())

# text = "Python"

# print(text.lower())
# print(text.upper())

#use case- 
# user = input("Enter yes/no: ")

# if user.lower() == "yes":
#     print("Confirmed")


# words = ["python","is","fun"]
# sentence = " ".join(words)
# print(sentence)
# print(sentence.replace("python", "java"))





#Checking Text
# isalpha()
# isdigit()
# isalnum()

#String Formatting - (f-strings)

# name = "Nigga"
# age = 23

# print(f"My name is {name} and age is {age}")






#Task-1

# sentence = input("Enter the sentence: ")

# words = sentence.split()

# print(f"Number of words: ", len(words))








#Task-2

# sentence = "Python makes coding easy"
# cap = sentence.upper()
# words = cap.split()
# print(words)








#Mini Project
username = "    Abhay_123   "
fix = username.strip()
low = fix.lower()
print(low)













