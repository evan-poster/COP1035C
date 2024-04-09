# Week1/program6.py
# Calculate the momentum and kinetic energy of an object

# Define a function to calculate the momentum of an object
def calculate_momentum(mass, velocity):
    return mass * velocity

# Define a function to calculate the kinetic energy of an object
def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity**2


# Get mass and velocity from the user
mass = float(input("Enter the mass of the object: "))
velocity = float(input("Enter the velocity of the object: "))

# Output the momentum and kinetic energy of the object
print(f"The momentum of the object is {calculate_momentum(mass, velocity)}.")
print(f"The kinetic energy of the object is {calculate_kinetic_energy(mass, velocity)}.")
