# Typecasting in Python is the process of converting a variable from one data type to another.

name="Abhishek"
age=22
gpa=3.8
#ypye() is used to check the data type of a variable
print(type(name))  # Output: <class 'str'>
print(type(age))   # Output: <class 'int'>
print(type(gpa))   # Output: <class 'float'>
age=str(age)  # Converting integer to string
gpa=int(gpa)  # Converting float to integer
print(type(age))  # Output: <class 'str'>
print(type(gpa))  # Output: <class 'int'>
print(f"My name is {name}, I am {age} years old and my GPA is {gpa}.")