# 1. Print the 4th element from first and 4th element from last in a tuple
sample_tuple = (5, 10, 15, 20, 25, 30, 35, 40)
print("4th element from the start:", sample_tuple[3])
print("4th element from the end:", sample_tuple[-4])

# 2. Check whether an element exists in a tuple or not
element = 25
if element in sample_tuple:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")

# 3. Convert a list into a tuple
sample_list = [1, 2, 3, 4, 5]
converted_tuple = tuple(sample_list)
print("Converted tuple:", converted_tuple)

# 4. Find the index of an item in a tuple
item_to_find = 30
if item_to_find in sample_tuple:
    index = sample_tuple.index(item_to_find)
    print(f"Index of {item_to_find} is:", index)
else:
    print(f"{item_to_find} not found in the tuple.")

# 5. Replace last value of tuples in a list to 100
sample_list_of_tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
updated_list = [t[:-1] + (100,) for t in sample_list_of_tuples]
print("Updated list of tuples:", updated_list)
