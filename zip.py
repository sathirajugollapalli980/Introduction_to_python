
answers = ["b", "a", "d", "c"]
correct = ["b", "c", "d", "c"]

score = 0

for answer, solution in zip(answers, correct):
    if answer == solution:
        score += 1

print(f"Score: {score}/4")
