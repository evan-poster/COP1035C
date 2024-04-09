# Calculate the area of a rectangle based on the width and height entered by the user

# Define a function to calculate the area of a rectangle
def rectangle_area(w, h):
    return w * h

# Greet user and say what we are doing
print("Hello, welcome to the rectangle area calculator!")
print("Please provide the following information:")

# Prompt user to enter width and height, store it in variables
width = float(input("Enter the width: "))
height = float(input("Enter the height: "))

# Output the area to the user
print(f"The area is of a {width} x {height} rectangle is", rectangle_area(width, height), "square units.")
