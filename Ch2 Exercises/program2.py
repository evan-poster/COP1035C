# Week1/Ch2 Exercises/program2.py
# Calculate the surface area of a cube

# Define a function to calculate the surface area of a cube
def surface_area(length):
    # Parenthesis for clarity; it's not necessary here due to order of operations
    area = 6 * (length ** 2)
    return area

# Get the length of the cube from the user
length = float(input("Enter the length of the cube: "))

# Output the surface area of the cube
print(f"The surface area of the cube is {surface_area(length)}")
