def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2

def multiply_numbers(num1, num2):
    return num1 * num2

def divide_numbers(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero!")
    return num1 / num2

if __name__ == "__main__":
    print("Welcome to the Calculator")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print("Choose operation: \n1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    operation = input("Enter operation (1/2/3/4): ")

    if operation == "1":
        result = add_numbers(num1, num2)
        operation_name = "addition"
    elif operation == "2":
        result = subtract_numbers(num1, num2)
        operation_name = "subtraction"
    elif operation == "3":
        result = multiply_numbers(num1, num2)
        operation_name = "multiplication"
    elif operation == "4":
        result = divide_numbers(num1, num2)
        operation_name = "division"
    else:
        print("Invalid operation selected.")
        exit()

    print(f"The result of {operation_name} between {num1} and {num2} is {result}.")
