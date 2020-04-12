fruits = ["apple", "oranges", "grapes", "apple"]
print("fruits[] : " + str(fruits))

# 1. accessing individual elements in the list
# a. Using positive indexes in the list
print("\nAccessing items in a list..")
print("fruits[] : " + str(fruits[0]) + "," + fruits[1].title() + "," + fruits[2])
# b. Using negative indexes in the list
print("fruits[] : " + fruits[-1] + "," + fruits[-2] + "," + fruits[-3].upper())

# 2. Adding elements in a list
# a. modifying a list
print("\nInserting items in a list..")
fruits[1] = "mangoes"
print("modified fruits[] : " + str(fruits))
# b. appending to a list
fruits.append("pineapples")
print("appended fruits[] : " + str(fruits))
# c. inserting in a list
fruits.insert(-3, "oranges")
fruits.insert(3, "kiwis")
print("inserted fruits[] : " + str(fruits))

# 3. Copying elements from a list into another list
print("\nCopying items from a list..")
fruits_copy = fruits.copy()
print("copied fruits[]  : " + str(fruits_copy))

# 4. Deleting elements in a list
# a. deleting a particular item, with no access to the deleted item
print("\nDeleting items from a list..")
del fruits[4]
print("deleted fruits[]  : " + str(fruits))
# b. removes the last item from the list
deleted_item = fruits.pop()
print("deleted fruits[]  : " + str(fruits))
print("deleted item : " + deleted_item)
# c. removes a particular item from the list and getting hold of the deleted item
deleted_item = fruits.pop(2)
print("deleted fruits[]  : " + str(fruits))
print("deleted item : " + deleted_item)
# d. deleting by value
item_to_delete = "apple"
print("item to Delete : " + item_to_delete)
fruits.remove(item_to_delete)
print("deleted fruits[]  : " + str(fruits))
# Copying a reference of list to another list
fruits = fruits_copy

# 5. Sorting elements in a list
print("\nSorting items in a list..")
# a. temporary sort
sorted_fruits = sorted(fruits)
print("temp Sorted fruits[] : " + str(sorted_fruits))
print("original fruits[]    : " + str(fruits))
# b. permanent sort
fruits.sort()
print("perm Sorted fruits[] : " + str(fruits))
print("original fruits[]    : " + str(fruits))

# 6. Reversing elements in a list
print("\nReversing items in a list..")
print("original fruits[] : " + str(fruits))
fruits.reverse()
print("reversed fruits[] : " + str(fruits))

# 7. Finding the length of a list
print("\nFinding length of a list..")
print("original fruits[]  : " + str(fruits))
length = len(fruits)
print("length of fruits[] : " + str(length))