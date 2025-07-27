
# 1.  Write a program to check if a given number is Positive, Negative, or Zero.
num = int(input("Enter a number: "))
if num > 0:
    print("The number is Positive.")
elif num < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")

# 2.  Write a program to check if a given number is odd or even.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")

# 3.Given two non-negative values, print true if they have the same last digit, such as with 27 and 57.
# lastDigit(7, 17) → true                                                
# lastDigit(6, 17) → false
# lastDigit(3, 113) → true
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a % 10 == b % 10:
    print("True")
else:
    print("False")

# 4.  Write a program to print numbers from 1 to 10 in a single row with one tab space.
for i in range(1, 11):
    print(i, end="\t")
print()

# 5.  Write a program to print even numbers between 23 and 57. Each number should be printed in a separate row
for i in range(23, 58):
    if i % 2 == 0:
        print(i)

# 6.  Write a program to check if a given number is prime or not.
num = int(input("Enter a number: "))
if num < 2:
    print("Not a prime number.")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Not a prime number.")
            break
    else:
        print("It is a prime number.")

# 7.  Write a program to print prime numbers between 10 and 99.
for num in range(10, 100):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

# 8.  Write a program to print the sum of all the digits of a given number.
# Example:
# I/P:1234
# O/P:10
num = int(input("Enter a number: "))
total = 0
while num > 0:
    digit = num % 10
    total += digit
    num //= 10
print("Sum of digits:", total)

# 9.  Write a program to reverse a given number and print.

# Example:1
# I/P: 1234
# O/P:4321

# Example:2
# I/P:1004
# O/P:4001
num = int(input("Enter a number: "))
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print("Reversed number:", reversed_num)

# 10. Write a program to find if the given number is palindrome or not

# Example:1
# I/P:110011
# O/P: 110011 is a palindrome.

# Example:2
# I/P:1234
# O/P: 1234 is not a palindrome.
num = int(input("Enter a number: "))
original = num
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
if original == reversed_num:
    print(f"{original} is a palindrome.")
else:
    print(f"{original} is not a palindrome.")
