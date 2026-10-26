a = float(input("First number: "))
op = input("Operator (+, -, *, /): ")
b = float(input("Second number: "))

if op == "+":
    print(f"{a} + {b} = {a + b}")
elif op == "-":
    print(f"{a} - {b} = {a - b}")
elif op == "*":
    print(f"{a} * {b} = {a * b}")
elif op == "/":
    if b == 0:
        print("Error: Division by zero is not allowed.")    
    else:
        print(f"{a} / {b} = {a / b}")
else:
    print("Error: Invalid operator")
