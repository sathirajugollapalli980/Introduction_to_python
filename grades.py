grade = float(input("Enter your grade: "))

if grade < 0 or grade >20:
    print("Invalid grade")
else:
    if grade >= 16:
        mention = "Very good"
    elif grade >= 14:
        mention = "Good"
    elif grade >= 12:
        mention = "Fairly good "
    elif grade >= 10:
        mention = "Pass"
    else:
        mention = "Fail"

    print("Your grade is:", grade)
    print("Mention:", mention)