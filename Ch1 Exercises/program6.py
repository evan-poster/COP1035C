# Calculate the area of a circle based on the radius entered by the user

# Define a function to calculate the area of a circle
def calculate_circle_area(radius):
    """
    Calculates the area of a circle given its radius.
    """
    return 3.14 * radius ** 2

# Greet user and explain what we're doing
print("Hello, welcome to the circle area calculator!")
print("Please provide the following information:")

# Prompt user to enter radius and store it in a variable
radius = float(input("Enter the radius of the circle: "))

# Output the area to the user
print("The area of the circle is", calculate_circle_area(radius), "square units.")
