# Week1/Ch2 Exercises/program4.py
# Calculate the diameter, circumference, surface area, and volume of a sphere
import math

# Get the radius of the sphere from the user
radius = float(input("Enter the radius of the sphere: "))

# Calculate the diameter, circumference, surface area, and volume of the sphere
diameter = 2 * radius
circumference = 2 * math.pi * radius
surface_area = 4 * math.pi * radius ** 2
volume = (4 / 3) * math.pi * radius ** 3

# Output the results to the user
print(f"Diameter: {diameter}")
print(f"Circumference: {circumference}")
print(f"Surface Area: {surface_area}")
print(f"Volume: {volume}")
