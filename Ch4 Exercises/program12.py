#!/usr/bin/env python3
# Week2/Ch4 Exercises/program12.py

'''
    File Format for Payroll:
    <last name> <hourly wage> <hours worked>
'''

# NOTE: This program looks in the current directory or takes an absolute path ONLY

# Prompt the user for the filename
filename = input("Enter the filename: ")

# Open the file and read its contents
with open(filename, 'r') as file:
    lines = file.readlines()

# Output a header for the report
print("Last Name\tHours\tWages")

# Output the report
for line in lines:
    employee_info = line.strip().split()
    name = employee_info[0]
    hours = float(employee_info[2])
    wage = float(employee_info[1]) * hours
    print(f"{name}\t\t{hours:.2f}\t${wage:.2f}")
