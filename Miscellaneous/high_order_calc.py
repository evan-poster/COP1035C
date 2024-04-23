
# Math Functions
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

# Dictionary of basic math operations and their relevant function
op_functions = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}

# Lambda Syntax
# lambda parameters: expression
op_functions_lambda = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

# Main function
def main():
    while True:
        # Ask user for basic math operation with two numbers
        user_input = input("Enter a basic math operation with two numbers (e.g. 3 + 4): ").split()

        # Check if user wants to quit
        if user_input == ['quit']:
            break

        # First and last elements are numbers
        num1 = float(user_input[0])
        num2 = float(user_input[-1])
        # The second element is the operation
        op = user_input[1]

        # Call relevant function from the dictionary
        result = op_functions[op](num1, num2)
        result_lambda = op_functions_lambda[op](num1, num2)

        # Print results
        print(f"{num1} {op} {num2} = {result}")
        print(f"{num1} {op} {num2} = {result_lambda} (lambda)")

# Entry Point
if __name__ == "__main__":
    main()
