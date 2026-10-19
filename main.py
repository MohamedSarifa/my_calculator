from calculator import calculate

print("Simple Python Calculator")

try:
    a = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    b = float(input("Enter second number: "))

    result = calculate(a, operator, b)
    print("Result:", result)

except ValueError as error:
    print("Error:", error)
