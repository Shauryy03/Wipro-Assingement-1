
# Program: Cube every number in the given list using lambda and map()

# Input list
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

cubed_list = list(map(lambda x: x ** 3, list_1))
print("Original List:", list_1)
print("Cubed List:", cubed_list)
