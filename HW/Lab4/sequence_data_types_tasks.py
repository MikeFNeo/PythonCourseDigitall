# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
    Write a program which will ask the user to enter 3 names.
	The names, should be stored into a list 'names'.
    Create another list 'sorted_name' which will have names, sorted alphabetically. Do not change the original 'names' list.

    TIP: use list.sort() method to sort a list. Note, that the sort() method works "in-place",
"""

### Your code here

# names = []
# names.append(input('Enter 1st name: '))
# names.append(input('Enter 2nd name: '))
# names.append(input('Enter 3rd name: '))

# sorted_name = names.copy()
# sorted_name.sort()

# print (f'Originally entered names: {names}')
# print (f'Sorted names: {sorted_name}')


### EXPECTED OUTPUT:
# Enter 1st name: Maria
# Enter 2nd name: Ivan
# Enter 3rd name: Asen

# Originally entered names:  ['Maria', 'Ivan', 'Asen']
# Sorted names: ['Asen', 'Ivan', 'Maria']


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
    Write a program that asks the user to enter a word and then checks if the word is a palindrome.
    A palindrome is a word that reads the same forward and backward, ignoring case.

    Tip: you can use str.lower() to convert a string to lowercase
"""

### Your code here

# word_str = input('Enter a word: ')
# word_list = list(word_str.lower())
# word_reverse_list = word_list.copy()
# word_reverse_list.reverse()

# if word_list == word_reverse_list:
#     print (f'The word {word_str} is a palindrome')
# else:
#     print (f'The word {word_str} is not a palindrome')

### EXPECTED OUTPUT:
# Enter a word : Racecar
# The word 'Racecar' is a palindrome

# Enter a word : car
# The word 'car' is not a palindrome