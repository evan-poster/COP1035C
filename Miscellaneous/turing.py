
name = "Alan Turing"

# Recursive function
def print_by_letter(name):
    print(name[0])
    if len(name) > 1:
        print_by_letter(name[1:])

print_by_letter(name)
