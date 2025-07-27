"""
1. Write a program to read the entire content from a txt file and display it to the user.
"""

with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)


"""
2. Write a program to read first n lines from a txt file. Get n as user input.
"""

n = int(input("Enter number of lines to read: "))

with open("sample.txt", "r") as file:
    for i in range(n):
        print(file.readline(), end='')


"""
3. Write a program to accept input from user and append it to a txt file.
"""

user_input = input("Enter text to append to file: ")

with open("sample.txt", "a") as file:
    file.write(user_input + "\n")

print("Text appended to file.")


"""
4. Write a program to read contents from a txt file line by line and store each line into a list.
"""

with open("sample.txt", "r") as file:
    lines = file.readlines()

print("Lines as list:", lines)


"""
5. Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.
"""

with open("sample.txt", "r") as file:
    words = file.read().split()

longest = max(words, key=len)
print("Longest word:", longest)


"""
6. Write a program to count the frequency of a user entered word in a txt file.
"""

word_to_count = input("Enter the word to count: ")

with open("sample.txt", "r") as file:
    text = file.read()

words = text.split()
count = words.count(word_to_count)

print(f"The word '{word_to_count}' occurs {count} times.")
