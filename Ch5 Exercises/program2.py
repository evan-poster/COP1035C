# ipsum.txt provided for testing
# Verify correct path!
filename = input("Enter the filename: ")

with open(filename) as file:
    lines = file.readlines()

while True:
    print(f"Number of lines in the file: {len(lines)}")
    line_num = int(input("Enter a line number (0 to quit): "))

    if line_num == 0:
        break

    if line_num > 0 and line_num <= len(lines):
        print(lines[line_num-1].strip())
    else:
        print("Invalid line number.")
