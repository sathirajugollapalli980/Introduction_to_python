
scores = [12, 17, 9, 15, 14]

best_score = 0
best_student = 0

for position, score in enumerate(scores, start=1):
    if score > best_score:
        best_score = score
        best_student = position

print(f"Best: {best_score} (student #{best_student})")
