# Week2/Ch3 Exercises/program2.py

# Get lengths of three sides of a triangle from the user
side_a = float(input("Enter the length of side A: "))
side_b = float(input("Enter the length of side B: "))
side_c = float(input("Enter the length of side C (the hypothenuse): "))

# Check if the triangle is a right triangle
# Uses the Pythagorean theorem: a^2 + b^2 = c^2
if (side_a ** 2 + side_b ** 2) == side_c ** 2:
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
