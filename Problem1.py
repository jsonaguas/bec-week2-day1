def calculator():
    operation = input("Please enter which operation you'd like to use (add,subtract,multiply,divide): ")
    if operation == "add":
        num1 = float(input("Enter 1st of 2nd number: "))
        num2 = float(input("Enter 2nd of 2nd number: "))
        print("Sum is ", add(num1, num2))
    elif operation == "subtract":
        num1 = float(input("Enter 1st of 2nd number: "))
        num2 = float(input("Enter 2nd of 2nd number: "))
        print("Difference is", subtract(num1, num2))
    elif operation == "multiply":
        num1 = float(input("Enter 1st of 2nd number: "))
        num2 = float(input("Enter 2nd of 2nd number: "))
        print("Product is", multiply(num1, num2))
    elif operation == "divide":
        num1 = float(input("Enter 1st of 2nd number: "))
        num2 = float(input("Enter 2nd of 2nd number: "))
        print("Quotient is", divide(num1, num2))

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero"

calculator()
