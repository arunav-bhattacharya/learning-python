fruits = ["apples", "oranges", "grapes", "watermelons"]
fruits.sort()
print(fruits)

# 1. Looping through a list
print("\nIterating through a list..")
i = 0
print("fruits[]")
# looping using items
print("Accessing each item in the list..")
# Always indent the line after the for statement in a loop. If you forget, Python will throw Indention error
# The colon at the end of a for statement tells Python to interpret the next line as the start of a loop.
for fruit in fruits:
    print("fruit[" + str(i) + "]=" + fruit)
    i = i + 1

# looping using range() function
print("\nAccessing elements using indexes..")
for i in range(0, len(fruits)):
    print(f"fruit[{i}]=" + fruits[i])

# Using a numerical range
print("\nNumbers in a range..")
for number in range(0, 20):
    print(number)

# Create a list of numbers
print("\nNumbers in a list..")
numbers = list(range(0, 10))
print(numbers)

# If a third argument is passed to range(), Python uses that value as a step size when generating numbers.
# Even numbers
print("\nEven Numbers in a Range..")
even_numbers = list(range(0, 10, 2))
print(even_numbers)

# Square numbers
# "**" represents power raised after a number
print("\nSquared Numbers in a Range..")
squares = []
for number in range(2, 10):
    squares.append(number ** 2)
print(squares)

# Sum basic math functions
print(f"\nMin in squares[] {min(squares)}")
print(f"Max in squares[] {max(squares)}")
print(f"Sum in squares[] {sum(squares)}")

# List comprehension
# A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element.
print("\nDefining a list by combining for loop and creation of new elements in a single line..")
squares = [number ** 2 for number in range(0, 10)]
print(squares)

# Slicing a list
# In order to slice a portion of the list you can use colon(:)
# Number before : is the starting index of the slice
# Number after : is the index-1 of the element, OR, the item in the list when counting the first element in the list as 1

sliced_fruits = fruits[1:3]
print(f"fruits[]={fruits}")
print(f"Sliced fruits[]={sliced_fruits}")
print(f"Slicing number of elements from the first element={fruits[:2]}")
print(f"Slicing from a particular index to end of list={fruits[1:]}")
print(f"Slicing last 2 elements of list={fruits[-2:]}")

# Looping through a slice
print("Looping through a slice of a list..")
for fruit in fruits[1:3]:
    print(fruit)

# Tuples
# You cannot modify an element in Tuple, but you can re-assign the variable
print("\nTuples")
dimensions = (100, 50)
print(dimensions[0])
print(dimensions[1])

# The below line of code will not work
# dimensions[0] = 20
# But the below line is fine
dimensions = (20, 50)
