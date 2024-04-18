
test_sets = [
    ("JAN 2001", 31),
    ("FEB 2001", 28),
    ("MAR 2001", 31),
    ("SEP 1752", 19),
    ("FEB 1900", 28),
    ("FEB 2000", 29),
    ("FEB 2004", 29),
    ("FEB 1700", 28),
    ("FEB 1800", 28),
    ("FEB 2100", 28),
]

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
    # Account for leap years and their exceptions
    if month_year[0] == "FEB":
        if int(month_year[1]) % 4 == 0:
            if int(month_year[1]) % 100 == 0:
                if int(month_year[1]) % 400 == 0:
                    return 29
                else:
                    return 28
            else:
                return 29
        else:
            return 28
    if month_year[0] == "SEP" and month_year[1] == "1752":
        return 19
    else:
        return my_table[month_year[0]]


if __name__ == "__main__":
    # data = input("Enter a month and year with format: FEB 2000: ").upper().strip().split()
    # print(days_in_month(data))
    pass_count = 0
    for test in test_sets:
        if days_in_month(test[0].split()) == test[1]:
            pass_count += 1
        else:
            print(f"FAIL ({test[0]})")
    if pass_count == len(test_sets):
        print("Passed all tests")
    else:
        print(f"Passed {pass_count} out of {len(test_sets)} tests")
