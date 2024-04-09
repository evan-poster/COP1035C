# Calculate the area of a triangle based on the base and height entered by the user

# Define a function to calculate the area of a triangle
def area_of_triangle(b, h):
    return 0.5 * b * h

# Greet user and explain what we're doing
print("Hello, welcome to the triangle area calculator!")
print("Please provide the following information:")

# Prompt user to enter base and height, store it in variables
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Output the area to the user
print("The area of the triangle is", area_of_triangle(base, height), "square units.")
