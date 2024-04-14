# Week3/Ch3 Exercises/program7.py

# Define a function to calculate the salary schedule
def calculate_salary_schedule(starting_salary, increase_percent, num_years):
    # Create a table to store the salary schedule
    salary_schedule = []

    # Add the first year to the table
    salary_schedule.append([1, starting_salary])

    # Calculate the salary for each additional year
    for year in range(2, num_years+1):
        # Calculate the salary for the current year
        salary = salary_schedule[year-2][1] * (1 + increase_percent/100.0)
        # Add the year and salary to the table
        salary_schedule.append([year, salary])

    # Output the salary schedule in tabular format
    for row in salary_schedule:
        print(f"{row[0]:<5}\t${row[1]:>10.2f}")

# Get user inputs
starting_salary = float(input("Enter the starting salary: "))
increase_percent = float(input("Enter the percentage increase: "))
num_years = int(input("Enter the number of years in the schedule: "))

# Print our table header
print("Year\tSalary")

# Call the function to calculate and display the salary schedule
calculate_salary_schedule(starting_salary, increase_percent, num_years)
