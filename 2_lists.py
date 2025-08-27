# List of fruits
fruits = ["apples", "oranges", "grapes", "watermelons"]
print(fruits)
print("fruits[]=" + str(fruits))

# 1. accessing individual elements in the list
# a. Using positive indexes in the list
# Index positions start at 0 and not 1
print("\nAccessing items in a list..")
print("fruits[] in asc order=" + str(fruits[0]) + "," + fruits[1].title() + "," + fruits[2])
# b. Using negative indexes in the list
# Negative indices refer to the elements in the reverse order in the list
# For example, -1 points to the last element, -2 second last element and so on..
print("fruits[] in desc order=" + fruits[-1] + "," + fruits[-2] + "," + fruits[-4].upper())

# 2. Adding elements in a list
# a. modifying a list
print("\nModifying items in a list..")
fruits[1] = "mangoes"
print("Modified fruits[]=" + str(fruits))
# b. appending to a list
fruits.append("pineapples")
print("Appended fruits[]=" + str(fruits))
# c. inserting in a list
fruits.insert(-3, "oranges")
print("Inserted oranges in fruits[]=" + str(fruits))
fruits.insert(3, "kiwis")
print("Inserted kiwis in fruits[]=" + str(fruits))

# 3. Copying elements from a list into another list
print("\nCopying items from a list..")
fruits_copy = fruits.copy()
print("copied fruits[]=" + str(fruits_copy))

# 4. Deleting elements in a list
# a. deleting a particular item, with no access to the deleted item
print("\nDeleting items from a list..")
del fruits[4]
print("Deleted 5th item in fruits[]=" + str(fruits))
# b. removes the last item from the list
deleted_item = fruits.pop()
print("Deleted last item in fruits[]=" + str(fruits))
print("Deleted item=" + deleted_item)
# c. removes a particular item from the list and getting hold of the deleted item
deleted_item = fruits.pop(2)
print("Deleted 3rd item in fruits[]=" + str(fruits))
print("Deleted item=" + deleted_item)
# d. deleting by value
item_to_delete = "apples"
print("Item to Delete=" + item_to_delete)
fruits.remove(item_to_delete)
print(f"Deleted {item_to_delete} from fruits[]=" + str(fruits))
# Copying a reference of list to another list
fruits = fruits_copy

# 5. Sorting elements in a list
print("\nSorting items in a list..")
# a. temporary sort, returns a new list
sorted_fruits = sorted(fruits)
print("Temp Sorted fruits[]=" + str(sorted_fruits))
print("Original fruits[]=" + str(fruits))
# b. permanent sort, modifies the existing list
fruits.sort()
print("Perm Sorted fruits[]=" + str(fruits))

# 6. Reversing elements in a list
print("\nReversing items in a list..")
print("Original fruits[]=" + str(fruits))
# reverse() modifies the existing list
fruits.reverse()
print("Reversed fruits[]=" + str(fruits))

# 7. Finding the length of a list
print("\nFinding length of a list..")
print("Original fruits[]=" + str(fruits))
length = len(fruits)
print("Length of fruits[]=" + str(length))