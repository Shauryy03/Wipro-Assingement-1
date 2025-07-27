# 1. Count the number of upper and lower case letters in a String
input_str = input("Enter a string: ")
upper_count = 0
lower_count = 0
for char in input_str:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)

# 2. Check whether a given String is Palindrome or not
input_str = input("Enter a string: ")
if input_str == input_str[::-1]:
    print(f"'{input_str}' is a palindrome.")
else:
    print(f"'{input_str}' is not a palindrome.")

# 3. Return n copies of the first 2 characters of the string, where n is the length of the string
input_str = input("Enter a string (length >= 2): ")
if len(input_str) >= 2:
    result = input_str[:2] * len(input_str)
    print("Result:", result)
else:
    print("String must be at least 2 characters long.")

# 4. Remove 'x' from start and end of the string if present
input_str = input("Enter a string: ")
if input_str.startswith('x'):
    input_str = input_str[1:]
if input_str.endswith('x'):
    input_str = input_str[:-1]
print("Result:", input_str)

# 5. Repeat the last n characters of the string n times
input_str = input("Enter a string: ")
n = int(input("Enter an integer (0 to length of string): "))
if 0 <= n <= len(input_str):
    result = input_str[-n:] * n
    print("Result:", result)
else:
    print("Invalid value of n.")
