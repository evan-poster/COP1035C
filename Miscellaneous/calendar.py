
my_table = {
    "JAN": 31,
    "FEB": 28,
    "MAR": 31,
    "APR": 30,
    "MAY": 31,
    "JUN": 30,
    "JUL": 31,
    "AUG": 31,
    "SEP": 30,
    "OCT": 31,
    "NOV": 30,
    "DEC": 31
}


# Report the number of days in the month
def days_in_month(month_year):
    # Account for leap year
    if month_year[0] == "FEB":
        if int(month_year[1]) % 4 == 0:
            if int(month_year[1]) % 400 == 0 or int(month_year[1]) % 100 != 0:
                return my_table.get(month_year[0]) + 1
            return my_table.get(month_year[0])
    return my_table.get(month_year[0])


if __name__ == "__main__":
    data = input("Enter a month and year with format: FEB 2000: ").upper().strip().split()
    print(days_in_month(data))
