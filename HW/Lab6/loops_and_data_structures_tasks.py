# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
    Write a program that takes an integer n and prints a triangle pattern of stars (*). The number of stars in the first line is 1, in the second line is 2, and so on up to n stars in the n-th line.
"""

### Your code here

# stars_number = int(input ('Enter stars number: '))

# for i in range(1, stars_number+1):
#     print (f'{"*" * i}')

### EXPECTED OUTPUT:
# Enter stars number: 4
# *
# **
# ***
# ****


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
    Write a script that prompts the user to enter words, one at a time.
    The user should continue to enter words until they enter '0'.
    After the user enters '0', the script should display all the words that start with a vowel (a, e, i, o, u).
"""

### Your code
# user_words = []

# while True:
#     word = input("Enter a word (or '0' to stop): ")

#     if word == '0':
#         break
#     else:
#         user_words.append(word)

# vowel_words = [word for word in user_words if word.lower()[0] in 'aeiou']

# if vowel_words:
#     print(f"Words starting with a vowel: {vowel_words}")
# else:
#     print("No words starting with a vowel.")


### EXPECTED OUTPUT:
# Enter a word (or '0' to stop): atom
# Enter a word (or '0' to stop): see
# Enter a word (or '0' to stop): end
# Enter a word (or '0' to stop): 0
# Words that start with a vowel: ['atom', 'end']


# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
    Write a script that takes a list of strings and returns a dictionary,
    where each key is a string length and each value is a list of strings of that length.
"""

### Given:
words = ["hello", "world", "python", "is", "fun", "and", "useful"]

### Your code here

# words_dict = {}

# for i in words:
#     len_word = len(i)

#     if len_word in words_dict:
#         words_dict[len_word].append(i)
#     else:
#         words_dict[len_word] = [i]

# print (words_dict)


### EXPECTED OUTPUT:
# {5: ['hello', 'world'], 6: ['python'], 2: ['is'], 3: ['fun', 'and'], 7: ['useful']}


# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
    In a supermarket inventory system, there are two sets of product categories:
    1. Categories that need refrigeration.
    2. Categories on sale this week.

    Write a script, which performs the following tasks:
    a. Find and print the categories that are both refrigerated and on sale.
    b. Find and print categories that are on sale but do not require refrigeration.
    c. Suggest new sale categories from the refrigerated items which are not yet on sale.

    Note: The category names are assumed to be in lowercase.
"""

### Given
refrigerated = {'dairy', 'meats', 'frozen foods', 'seafood', 'deli'}
sale = {'cereals', 'dairy', 'snacks', 'frozen foods', 'beverages'}

### Your code here

# print (f'Categories both refrigerated and on sale: {refrigerated & sale}')
# print (f'Sale categories not needing refrigeration: {sale - refrigerated}')
# print (f'Suggested new sale categories from refrigerated items: {refrigerated - sale}')

### EXPECTED OUTPUT:
# Categories both refrigerated and on sale: {'dairy', 'frozen foods'}
# Sale categories not needing refrigeration: {'snacks', 'beverages', 'cereals'}
# Suggested new sale categories from refrigerated items: {'seafood', 'deli', 'meats'}