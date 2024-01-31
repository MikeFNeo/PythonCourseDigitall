# variables
students_scores = {
    'Ivan' : 5.00,
    'Alex' : 3.50,
    'Maria' : 5.50,
    'Georgy' : 5.00
}

# calculate and print the best and worst student
scores_list = list(students_scores.values())
min_score = min(scores_list)
max_score = max(scores_list)

for student, score in students_scores.items():
    if score == max_score:
        print(f'{student} - {score}')

for student, score in students_scores.items():
    if score == min_score:
        print(f'{student} - {score:}')