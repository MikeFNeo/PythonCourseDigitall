# varables
text = 'apple and banana one apple one banana a red apple and a green apple'

# calculate the repeating words
words_list = text.split()
words_set = set(words_list)

for i in words_set:
    print(f'{i:<7}{words_list.count(i)}')