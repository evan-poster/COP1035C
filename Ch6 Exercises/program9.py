
# Read in the numbers from a file
with open('numbers.txt') as f:
    numbers = [float(line.strip()) for line in f]

# Compute the average of the numbers
average = sum(numbers) / len(numbers) if numbers else 0.0

# Print the average
print(average)

# Alternative version using map and reduce
from functools import reduce

average = reduce(lambda x, y: x + y, 
                 map(float, open('numbers.txt').readlines())) / len(numbers) if numbers else 0.0

print(average)

