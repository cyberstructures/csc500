#Basic program accepting two integer inputs and performing basic arithmetic operations
#Spencer Ingram CSC500 - Professor Dr. Joseph Issa Winter A term 2026
print("Enter two integers to perform basic arithmetic operations.")
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Perform basic arithmetic operations
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2 if num2 != 0 else "undefined (division by zero)"

# Display results
print(f"Sum: {num1} + {num2} = {sum_result}")
print(f"Difference: {num1} - {num2} = {difference}")
print(f"Product: {num1} * {num2} = {product}")
print(f"Quotient: {num1} / {num2} = {quotient:g}")