# Week2/Ch3 Exercises/program1.py

# Get lengths of three sides of a triangle from the user
side_a = float(input("Enter the length of side A: "))
side_b = float(input("Enter the length of side B: "))
side_c = float(input("Enter the length of side C: "))

# Check if the triangle is equilateral
if side_a == side_b and side_b == side_c:
    print("The triangle is equilateral.")
else:
    print("The triangle is not equilateral.")
