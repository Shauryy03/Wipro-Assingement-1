"""
Program 1: Accept two numbers as command line arguments and display their sum.
Usage:
    python command_line_sum.py 10 20
"""

import sys

if len(sys.argv) != 3:
    print("Usage: python command_line_sum.py <num1> <num2>")
else:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print("Sum:", num1 + num2)


"""
Program 2: Accept a welcome message through command line arguments and display the file name along with the welcome message.
Usage:
    python command_line_welcome.py "Hello, Aditya!"
"""

import sys

if len(sys.argv) != 2:
    print("Usage: python command_line_welcome.py <message>")
else:
    print(f"File Name: {sys.argv[0]}")
    print(f"Welcome Message: {sys.argv[1]}")


"""
Program 3: Accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.
Usage:
    python command_line_sum_primes.py 2 3 4 5 6 7 8 9 10 11
"""

import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

if len(sys.argv) != 11:
    print("Usage: python command_line_sum_primes.py <10_numbers>")
else:
    numbers = list(map(int, sys.argv[1:]))
    prime_sum = sum(n for n in numbers if is_prime(n))
    print("Sum of prime numbers:", prime_sum)
