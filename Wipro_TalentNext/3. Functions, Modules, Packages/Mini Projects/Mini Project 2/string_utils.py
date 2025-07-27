# string_utils.py

def ispalindrome(name):
    name = name.replace(" ", "").lower()
    if name == name[::-1]:
        print("Yes it is a palindrome.")
    else:
        print("No it is not a palindrome.")

def count_the_vowels(name):
    name = name.lower()
    vowels = "aeiou"
    count = sum(name.count(v) for v in vowels)
    print("No of vowels:", count)

def frequency_of_letters(name):
    name = name.replace(" ", "").lower()
    freq = {}
    for char in name:
        freq[char] = freq.get(char, 0) + 1
    freq_output = ', '.join(f"{k}-{v}" for k, v in sorted(freq.items()))
    print("Frequency of letters:", freq_output)
