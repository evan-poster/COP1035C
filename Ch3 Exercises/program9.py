# Week2/Ch3 Exercises/program9.py

# Prompt user for inputs
numbers = []
while True:
    num = input("Enter a number: ")
    if num == '':  # Break loop if user presses enter key
        break
    numbers.append(float(num))

# Calculate sum and average
sum_numbers = sum(numbers)
avg = sum_numbers / len(numbers)

# Output results
print(f"Sum of numbers: {sum_numbers}")
print(f"Average of numbers: {avg:.2f}")
