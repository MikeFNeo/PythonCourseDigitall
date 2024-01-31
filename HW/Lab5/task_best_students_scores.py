# variables
students_scores = {
    'Ivan' : 5.00,
    'Alex' : 3.50,
    'Maria' : 5.50,
    'Georgy' : 5.00
}
best_students_scores = students_scores.copy()

# calculate and best students scores
for student, score in students_scores.items():
    if float(score) <= 4.00:
        best_students_scores.pop(student)

for student, score in best_students_scores.items():
    print (f'{student:<8} - {score:.2f}')