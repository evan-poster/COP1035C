'''
    STUDENT NOTE:
    The instructions are unclear to me.
    It does not specify if we are hard-coding the information
    or if we are asking the user to enter the information.
    I assume we are asking the user since it is the more complex process.
'''

# Tell user what we are doing
print("Please fill out the following information:")

# Prompt the user for their name, address, and telephone number and store it in a variable
name = input("Enter your name: ")
address = input("Enter your address: ")
telephone = input("Enter your telephone number: ")

# Output the user's information, each on their own line
print("Here is your information:")
print(f"Name: {name}")
print(f"Address: {address}")
print(f"Telephone: {telephone}")
