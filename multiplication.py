

n = int(input("Enter a number: "))

# Print the multiplication table
print("Table of:", n)

for i in range(1, 11):
    result = n * i
    print(f"{n} x {i} = {result}")
