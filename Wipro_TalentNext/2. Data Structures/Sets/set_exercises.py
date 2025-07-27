# 1. Remove a given item from the set
my_set = {10, 20, 30, 40, 50}
item_to_remove = 30

if item_to_remove in my_set:
    my_set.remove(item_to_remove)
    print(f"Updated set after removing {item_to_remove}:", my_set)
else:
    print(f"{item_to_remove} not found in the set.")

# 2. Create an intersection of sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersection = set1 & set2
print("Intersection of set1 and set2:", intersection)

# 3. Create a union of sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print("Union of set1 and set2:", union_set)

# 4. Find the maximum and minimum value in a set
my_set = {10, 25, 5, 80, 45}
max_val = max(my_set)
min_val = min(my_set)
print("Maximum value in the set:", max_val)
print("Minimum value in the set:", min_val)
