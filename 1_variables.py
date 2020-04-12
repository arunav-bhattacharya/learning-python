message = "Hello World of Python3 !"
print(message)

# 1. String basics
# ================
# string in-built functions
print("title: " + message.title())
print("lower :" + message.lower())
print("upper: " + message.upper())
# stripping white spaces
str1 = "  Mady's work is exceptional.   "
str2 = " Continue the good work Mady."
print(str1.rstrip().lstrip() + str2)

# string concat
first_name = "Arunav"
last_name = "Bhattacharya"
print("Hello !!\n" + first_name + " " + last_name)

# 2. Numbers basics
# =================
i = 2
j = 3.6
print("Add=" + str(i + j))
print("Sub=" + str(i - j))
print("Mul=" + str(i * j))
print("Div=" + str(i / j))

