
def divide(a, b):
    return a / b

def mod(a, b):
    '''Python-PowerPoint-Files.zip'''
    return a % b

def pow(a, b):
    return a ** b

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

print(f'{number1} divided by {number2} is {divide(number1, number2)}')
print(f'The remainder of {number1} divided by {number2} is {mod(number1, number2)}')
print(f'{number1} to the power of {number2} is {pow(number1, number2)}')

import mylib

mylib.hello()
