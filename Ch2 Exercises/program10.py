# Week1/Ch2 Exercises/program10.py
# Calculate total weekly pay

# Get the hourly wage, regular hours, and overtime hours from the user
hourly_wage = float(input("Enter hourly wage: "))
regular_hours = float(input("Enter total regular hours: "))
overtime_hours = float(input("Enter total overtime hours: "))

# Calculate total weekly pay
total_regular_pay = hourly_wage * regular_hours
overtime_pay = overtime_hours * (hourly_wage * 1.5)
total_weekly_pay = total_regular_pay + overtime_pay

# Output the total weekly pay
print(f"Total weekly pay: ${total_weekly_pay:.2f}")
