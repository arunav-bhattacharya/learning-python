message = "Hello World of Python3 !"
print(message)

# 1. String basics
# ================
# string in-built functions
print("title: " + message.title())  # Capitalize first letter of each word
print("lower :" + message.lower())  # lowercase every letter in the string
print("upper: " + message.upper())  # uppercase every letter in the string

# stripping white spaces
# Strip white spaces from right of string using rstrip()
# Strip white spaces from left of string using lstrip()
str1 = "  Mady's work is exceptional.   "
str2 = "     Continue the good work Mady."
print(str1.rstrip().lstrip() + " " + str2.lstrip())

# string concat
# You can use a single/double apostrophe for defining strings
first_name = 'Arunav'
last_name = "Bhattacharya"
book = "'s book"  # When you have a single quote within double quotes, Python interpreter recognizes it, but when used within single quotes it doesn't
print("Hello !!\n" + first_name + " " + last_name + book)

# 2. Numbers basics
# =================
i = 2
j = 3.6  # Any number with a decimal is a float
k = 6
print("Add=" + str(i + j))
print("Sub=" + str(i - j))
print("Mul=" + str(i * j))
print("Div=" + str(i / j))
print("Div=" + str(k / i))  # If you divide integers and the result is also a integer, but Python converts it as float

# Underscore in numbers & multiple variable assignment
num1, num2, num3 = 1_000_000, 5, 896_786.89
print(num1, num2, num3)

# Constants - Python doesn't have a constant variable but developers use capital letters separated with underscore to denote variables as constants

# Zen of Python
import this

# The Zen of Python, by Tim Peters
#
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!