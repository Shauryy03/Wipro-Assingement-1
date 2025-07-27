# Project: Command Line Arguments - Happiness Calculator

# Through command line arguments, three strings separated by space are given to you.
# Each string is a series of numbers separated by hyphen (-).
# You like all the numbers in string 1 and dislike all the numbers in string 2.
# Third string contains the numbers given to you.
# Your initial happiness is 0.
# When you encounter a number which is present in string 1, add 1 to your happiness.
# If it is present in string 2, add -1 to your happiness.
# Otherwise, your happiness does not change.
# Output your final happiness at the end.
# Sample input 1: 3-15-7 1-5-3-8
# Sample output 1: 1
# Sample input 2: 60-77-34-5-2 44-11-99-3 77-15-13-2-34-3
# Sample output 2: 2

import sys

if len(sys.argv) != 4:
    print("Usage: python script.py <like_string> <dislike_string> <given_string>")
    sys.exit(1)

like_str = sys.argv[1]
dislike_str = sys.argv[2]
given_str = sys.argv[3]

like_set = set(map(int, like_str.split('-')))
dislike_set = set(map(int, dislike_str.split('-')))
given_list = list(map(int, given_str.split('-')))

happiness = 0
for num in given_list:
    if num in like_set:
        happiness += 1
    elif num in dislike_set:
        happiness -= 1

print(happiness)
