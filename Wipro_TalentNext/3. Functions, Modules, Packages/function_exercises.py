"""
1. Write a function to return the sum of all numbers in a list.
Sample List: (8, 2, 3, 0, 7)
Expected Output: 20
"""

def sum_of_list(numbers):
    return sum(numbers)

# Example usage:
sample = [8, 2, 3, 0, 7]
print("Sum of list:", sum_of_list(sample))


"""
2. Write a function to return the reverse of a string.
Sample String: "1234abcd"
Expected Output: "dcba4321"
"""

def reverse_string(s):
    return s[::-1]

# Example usage:
print("Reversed string:", reverse_string("1234abcd"))


"""
3. Write a function to calculate and return the factorial of a number (a non-negative integer).
"""

def factorial(n):
    if n < 0:
        return "Invalid input"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage:
print("Factorial of 5:", factorial(5))


"""
4. Write a function that accepts a string and prints the number of upper and lower case letters in it.
"""

def count_case_letters(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    print(f"Uppercase letters: {upper}")
    print(f"Lowercase letters: {lower}")

# Example usage:
count_case_letters("Hello World!")


"""
5. Write a function to print the even numbers from a given list.
Sample List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result: [2, 4, 6, 8]
"""

def get_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

# Example usage:
print("Even numbers:", get_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))


"""
6. Write a function that takes a number as a parameter and checks whether the number is prime or not.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage:
print("Is 7 prime?", is_prime(7))
print("Is 10 prime?", is_prime(10))
