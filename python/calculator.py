num1 = float(input("Enter the first number: "))
num2 = float(input("enter second nummber: "))
operator = input("Enter Operation (+, -, *, /): ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    result = "invalid operator!"

print(f"{num1} {operator} {num2} = {result}")