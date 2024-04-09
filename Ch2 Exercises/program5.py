# Week1/Ch2 Exercises/program5.py
# Calculate momentum of an object

# Define a function to calculate the momentum of an object
def calculate_momentum(mass, velocity):
    return mass * velocity

# Get mass and velocity from the user
mass = float(input("Enter the mass of the object in kilograms: "))
velocity = float(input("Enter the velocity of the object in meters per second: "))

# Output the momentum of the object
print(f"The momentum of the object is {calculate_momentum(mass, velocity)}.")
