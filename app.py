# HELLO WORLD
import math


print("Hello World")
# IF I PUT "ANY WORD" * NUMBER IT WILL WRITE BY THE NUMBER U PUT IN
print("*" * 10)
# SHIFT + ALT + F FORMATS YOUR CODE
2 + 32
x = 1
y = 2
counter_strike2 = "gun_fight"
# PYTHON IMPLEMENTATIONS
# jython (java); IronPython (c#); PyPy (subset of python);
# what is an expression? -> An expression in python is a combination of operators and operands. (x = x; x = 10; a = x - 10)
# What is a syntax error? ->((bad grammar or wrong syntax in code)) is when we have a wrong line of code, so the interpreter won't be able to fully understand the code, like print "word" is missing the parentheses () between ("word")
# What does a linter do? -> a linter is a tool that check potential errors mostly in syntax errors

# VARIABLES
# kinds of data numbers booleans and strings
students_count = 1000  # Integer
rating = 4.99  # Float or Floating point number
is_published = True  # Booleans (True or False)
course_name = "Python programming"
print(students_count)
# Variable names
# cannot have space between the variable names like course name
# dont rely to much on the format tool, always try to write clean and beautiful code
# don't name the variable with mystical names like r1 = 4.99
# STRINGS
class_name = "Aquarius Class"
print(len(class_name))  # use len to find how many strings the variable have
# use [] to see what is the word in the index. Many programming languages starts with 0
print(class_name[0])
# negative index show the last word of the string and so on
print(class_name[-1])
# : show between index 0 to 4 (the number u put in is not showed)
print(class_name[0:5])
fruits_names = """banana, apple, pineapple, strawberry 
"\"my favorite\" is coconut
a"""
print(fruits_names)
# FORMATTED STRINGS
first_name = "Bruno"
last_name = "Vinicius"
full_name = f"{len(first_name)} {last_name}"
print(full_name)
# STRING METHODS
video_graphics = "Geforce RTX"
print(video_graphics.upper())
print(video_graphics.lower())
print(video_graphics.title())
# removes the space at the beginning and at the end
print(video_graphics.rstrip())
# finds the index for the word u put in (-1) if is false
print(video_graphics.find("RTX"))
print(video_graphics.replace("e", "a"))
print("RTX" in video_graphics)  # Search the word and returns boolean
# Search if does'nt have "rtx" in video_graphics (this is true)
print("rtx" not in video_graphics)
print(math.ceil(2.05))
# FUNDAMENTALS OF PROGRAMMING
# COMPARISON OPERATORS
# CONDITIONAL STATEMENTS
temperature = -15
if temperature > 35:
    print("It's warm as fuck!")
    print("Drink water!")
elif temperature > 20:
    print("It's normal, don't poop, even smell")
else:
    print("Cold as fuck! Warm yourself!")
print("Done")
# Ternary Operator
age = 22
#if age >= 18:
#    message = "Eligible"
#else:
#    message = "Not Eligible"
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)
# Logical Operators (and, or, not)
high_income = True
good_credit = True
student = False, 22
if (high_income and good_credit) and not student:
    print("You're Eligible to receive the loan")
else:
    print("Clean your name first!")
if student < 18 or True: print("You're not an adult!")
elif student >= 18:
    print("You have 18 yo")

