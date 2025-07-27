
# 1. Add a key and value to a dictionary
sample_dict = {0: 10, 1: 20}
sample_dict[2] = 30
print("Updated Dictionary:", sample_dict)

# 2. Concatenate multiple dictionaries to create a new one
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
merged_dict = {**dic1, **dic2, **dic3}
print("Merged Dictionary:", merged_dict)

# 3. Check if a given key already exists in a dictionary
key_to_check = 2
if key_to_check in sample_dict:
    print(f"Key {key_to_check} exists in the dictionary.")
else:
    print(f"Key {key_to_check} does not exist in the dictionary.")

# 4. Iterate over a dictionary and print keys, values, and both
example_dict = {'a': 1, 'b': 2, 'c': 3}
print("Keys:")
for key in example_dict:
    print(key)
print("Values:")
for value in example_dict.values():
    print(value)
print("Keys and Values:")
for key, value in example_dict.items():
    print(f"{key}: {value}")

# 5. Prepare a dictionary of numbers from 1 to 15 with their squares
squares_dict = {x: x**2 for x in range(1, 16)}
print("Dictionary of squares from 1 to 15:", squares_dict)

# 6. Sum all the values in a dictionary
sum_dict = {'a': 100, 'b': 200, 'c': 300}
total = sum(sum_dict.values())
print("Sum of all values:", total)
