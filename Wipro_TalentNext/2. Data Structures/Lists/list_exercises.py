
# 1. Create a list of 5 integers and display the list items. Access elements by index.
numbers = [10, 20, 30, 40, 50]
print("List:", numbers)
print("First element:", numbers[0])
print("Second element:", numbers[1])
print("Third element:", numbers[2])
print("Fourth element:", numbers[3])
print("Fifth element:", numbers[4])

# 2. Append a new item to the end of the list.
numbers.append(60)
print("After appending 60:", numbers)

# 3. Reverse the order of the items in the list.
numbers.reverse()
print("Reversed list:", numbers)

# 4. Print the number of occurrences of a specified element in a list.
element = 20
count = numbers.count(element)
print(f"Number of occurrences of {element}:", count)

# 5. Append the items of list1 to list2 in the front.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list2 = list1 + list2
print("After appending list1 to the front of list2:", list2)

# 6. Insert a new item before the second element in an existing list.
my_list = [100, 200, 300]
my_list.insert(1, 150)
print("After inserting 150 before second element:", my_list)

# 7. Remove the item from a specified index in a list.
index_to_remove = 2
if 0 <= index_to_remove < len(my_list):
    removed = my_list.pop(index_to_remove)
    print(f"Removed item at index {index_to_remove} ({removed}):", my_list)
else:
    print("Invalid index.")

# 8. Remove the first occurrence of a specified element from a list.
element_to_remove = 150
if element_to_remove in my_list:
    my_list.remove(element_to_remove)
    print(f"After removing first occurrence of {element_to_remove}:", my_list)
else:
    print(f"{element_to_remove} not found in the list.")
