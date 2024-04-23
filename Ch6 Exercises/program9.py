from functools import reduce

def main():
    # Read in the numbers from a file
    with open('numbers.txt') as f:
        numbers = [float(line.strip()) for line in f]

    average = reduce(lambda x, y: x + y, map(float, open('numbers.txt').readlines())) / len(numbers) if numbers else 0.0

    print(average)


if __name__ == "__main__":
    main()
