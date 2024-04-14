import sys

def mean(numbers):
    """Compute the average of a list of numbers"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    """Compute the median of a list of numbers"""
    if not numbers:
        return 0
    sorted_numbers = sorted(numbers)
    if len(numbers) % 2 == 1:
        return sorted_numbers[len(numbers) // 2]
    midpoint = len(numbers) // 2
    return (sorted_numbers[midpoint - 1] + sorted_numbers[midpoint]) / 2

def mode(numbers):
    """Compute the mode of a list of numbers"""
    if not numbers:
        return 0
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    max_count = max(counts.values())
    modes = [num for num, count in counts.items() if count == max_count]
    return sorted(modes)[0]

def main():
    """Test the three statistical functions"""
    numbers = [float(num) for num in input("Enter a list of numbers separated by whitespace: ").split()]
    print(f"Mean: {mean(numbers)}")
    print(f"Median: {median(numbers)}")
    print(f"Mode: {mode(numbers)}")

if __name__ == '__main__':
    main()
