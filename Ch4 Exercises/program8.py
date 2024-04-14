#!/usr/bin/env python3
# Week2/Ch4 Exercises/program8.py

# NOTE: This program looks in the current directory or takes an absolute path ONLY

# Prompt the user for the names of two text files
source_file = input("Enter the name of the file to copy from: ")
destination_file = input("Enter the name of the file to copy to: ")

# Open the source file and read its contents
with open(source_file, "r") as input_file:
    contents = input_file.read()

# Write the contents to the destination file
with open(destination_file, "w") as output_file:
    output_file.write(contents)

# Notify the user the copy is complete
print(f"'{source_file}' has been copied to '{destination_file}'.")
