#File Handling

#Syntax
# file = open("filename", "mode")

#Modes
# | Mode | Meaning      |
# | ---- | ------------ |
# | r    | read         |
# | w    | write        |
# | a    | append       |
# | r+   | read + write |


#Reading a File

# file = open("README.md", "r")
# content = file.read()
# print(content)
# file.close()



#Writing/Creating/Overwriting a File
# file = open("notes.txt", "w")
# file.write("Hello Abhay")
# file.close()


#Append Mode -> Append means add data without deleting existing data.
# file = open("notes.txt", "a")
# file.write("\nLearning Python")
# file.close()


#Modern Python -> Because Python automatically closes the file.
# with open("notes.txt", "r") as file:
#     content = file.read()
#     print(content)


#Student Record Writer
# with open("notes.txt", "a") as file:
#     content = file.write(input("Enter note: "))
#     print("Saved successfully!")



#Student Record Program

name = input("Enter Name: ")
age = input("Enter Age: ")
marks = input("Enter Marks: ")

with open("students.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Marks: {marks}\n")

print("Student record saved successfully.")


#NOTE
# f"  " -> is called f-string in python
# f before a string means formatted string.
# it allows you to insert variables directly inside the string using{} 
# eg. f"Name: {name}"

    