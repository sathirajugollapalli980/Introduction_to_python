
n = int(input("Enter a whole number: "))

# Start by assuming the number is prime
is_prime = n >= 2

# Check every possible divisor
for d in range(2, n):
    if n % d == 0:
        print(f"{n} is divisible by {d}")
        is_prime = False
        break

# Print the result
if is_prime:
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")  
