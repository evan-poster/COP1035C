# Week2/Ch3 Exercises/program6.py

# Approximate π using Leibniz's formula

# Get number of iterations from the user, store it in a variable
iterations = int(input("Enter the number of iterations: "))

# Calculate π using Leibniz's formula
result = 0.0
sign = 1.0
for i in range(1, iterations+1):
    result += sign / (2*i-1)
    sign *= -1

# Output the approximation of π
print(f"The approximation of π using Leibniz's formula with {iterations} iterations is {4*result:.50f}")
