
weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))

# Calculate BMI
bmi = weight / height ** 2

# Determine the category
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

# Print BMI with one decimal
print(f"BMI: {bmi:.1f} ({category})")
