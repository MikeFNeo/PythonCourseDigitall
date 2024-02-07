# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
Write a function named 'calculate_area' that takes two parameters (length and width)
and returns the area of a rectangle.
"""

### Your code here

# calculate_area = lambda l, w: l * w
# print(calculate_area(10, 5)) 

### EXPECTED OUTPUT:
# calculate_area(10, 5) should return 50


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
Create a function 'is_even' that takes a single integer argument and returns True
if the number is even, and False otherwise.
"""

### Your code here

# is_even = lambda x: x % 2 == 0
# print(is_even(4))
# print(is_even(5))

### EXPECTED OUTPUT:
# is_even(4) should return True
# is_even(5) should return False


# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
Write a lambda function 'add' that takes two arguments and returns their sum.
"""

### Your code here

# add = lambda a, b: a + b

# print(add(2, 3))

### EXPECTED OUTPUT:
# add(2, 3) should return 5


# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
Write a function named 'convert_temperature' that takes two parameters:
a temperature and the unit ('C' for Celsius, 'F' for Fahrenheit).
The function should convert the temperature to the other unit and return it.
"""

### Your code here

# convert_temperature = lambda x, t: f'{(x * (9/5)) + 32} (Fahrenheit)' if t != 'F' else f'{(x - 32) * 5/9} (Celsius)'

# print(convert_temperature(32, 'C'))
# print(convert_temperature(89.6, 'F'))

### EXPECTED OUTPUT:
# convert_temperature(32, 'C') should return 89.6 (Fahrenheit)
# convert_temperature(89.6, 'F') should return 32 (Celsius)


# ---------------------------------- Task 5 ---------------------------------- #
""" DESCRIPTION:
Create a function 'filter_words' that takes a list of words and a minimum length, and
returns a list of words that are longer than the given minimum length.
"""

### Your code here

# def filter_words(x, y):
#     x[:] = [word for word in x if len(word) >= y]

# words = ["apple", "pear", "banana", "cherry"]
# filter_words(words, 5)
# print(words)

### EXPECTED OUTPUT:
# filter_words(["apple", "pear", "banana", "cherry"], 5) should return ['banana', 'cherry']


# ---------------------------------- Task 6 ---------------------------------- #
""" DESCRIPTION:
Write a lambda expression 'sort_by_last_letter' that sorts a list of strings based on
the last letter of each string. Use this lambda expression to sort a given list,
using the sorted() built-in function.
"""

### Your code here

sort_by_last_letter = lambda x: x[-1]

string_list = ['apple', 'banana', 'cherry']

sorted_list = sorted(string_list, key=sort_by_last_letter)

print(sorted_list)


### EXPECTED OUTPUT:
# sort_by_last_letter(["banana", "apple", "cherry"]) should return ['banana', 'apple', 'cherry']