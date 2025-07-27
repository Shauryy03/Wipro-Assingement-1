# Project 1: Sort hyphen-separated colors alphabetically

def sort_colors(color_string):
    colors = color_string.split('-')
    colors.sort()
    return '-'.join(colors)

# Example usage
input1 = "green-red-yellow-black-white"
print(sort_colors(input1))  # Output: black-green-red-white-yellow

input2 = "PINK-BLUE-TAN-PURPLE"
print(sort_colors(input2))  # Output: BLUE-PINK-PURPLE-TAN


