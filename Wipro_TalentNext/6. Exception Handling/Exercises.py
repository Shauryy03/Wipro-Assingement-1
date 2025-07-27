"""
1. Accept two numbers and perform division with exception handling
"""
# Program to accept two numbers and perform division
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print("Result of division:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numbers.")
    
    

"""
2. Accept a number and check if it’s prime. Handle non-numeric input
"""
# Program to check if a number is prime with exception handling
try:
    num = int(input("Enter a number: "))
    if num < 2:
        print(f"{num} is not a prime number.")
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print(f"{num} is not a prime number.")
                break
        else:
            print(f"{num} is a prime number.")
except ValueError:
    print("Error: Invalid input. Please enter an integer.")
    
    

"""
3. Open a file and print its contents in title case
"""
# Program to open a file and print content in title case
try:
    filename = input("Enter file name: ")
    with open(filename, 'r') as file:
        content = file.read()
        print(content.title())
except FileNotFoundError:
    print("Error: File not found.")
    
    

"""
4. Check if number at an index in list is positive or negative with exception handling
"""
# Program to check if the number at a given index is positive or negative
numbers = [12, -7, 5, -3, 8, -1, 0, 4, -6, 9]

try:
    index = int(input("Enter an index (0-9): "))
    value = numbers[index]
    if value > 0:
        print(f"The number at index {index} is positive.")
    elif value < 0:
        print(f"The number at index {index} is negative.")
    else:
        print(f"The number at index {index} is zero.")
except IndexError:
    print("Error: Index out of range. Please enter a value between 0 and 9.")
except ValueError:
    print("Error: Please enter a valid integer.")

