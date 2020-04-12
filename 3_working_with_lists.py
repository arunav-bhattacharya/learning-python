fruits = ["apple", "oranges", "grapes", "apple"]

# 1. Looping through a list
print("\nIterating through a list..")
i = 0
print("printing fruits[]")
# looping using items
for fruit in fruits:
    print("fruit[" + str(i) + "] : " + fruit)
    i = i + 1
# looping using range
print("printing using indexes...")
for i in range(0, len(fruits)):
    print("fruit[" + str(i) + "] : " + fruits[i])