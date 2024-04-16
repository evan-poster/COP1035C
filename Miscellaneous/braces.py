
tests = [
    ["{}", True],
    ["}", False],
    ["{", False],
    ["}{", False],
    ["}}", False],
    ["{{}}", True],
    ["{{{}}}", True],
    ["{{}{}}", False],
    ["{{}}}", False],
    ["{{}", False],
    ["{}]", True],
    ["[{}]", True],
    ["[{]}", True],
    ["abc{}", True],
    ["abc{}def", True],
    ["abc{def", False],
    ["{{{}}{}}", False],
    ["{{{{{}}}}}", True],
]

# Function that takes a string of curly braces, possibly mixed with other characters
# Returns true if all pairs are closed properly
def checkBraces(string, clean=False):
    if clean:
        # Check if string size is even; odd means we have an open pair
        if len(string) % 2 > 0:
            return False
        # If we pass this, we've checked all pairs successfully
        if string == ["{","}"]:
            return True
        # If our string isn't a pair, it has to be len > 2 or we have a fail case
        if len(string) > 2:
            # If string starts and stops with {}, go to next level
            if string.pop(0) == '{' and string.pop() == '}':
                return checkBraces(string, True)
        return False
    else:
        # Our string may have characters we aren't checking
        # Remove them all with a for loop
        new_string = list()
        for char in string:
            if char in '{}':
                new_string.append(char)
        return checkBraces(new_string, True)


def checkBraces_unsafe(string):
    if len(string) % 2 > 0:
        return False
    if string == "{}":
        return True
    if len(string) > 2:
        if string[0] == '{' and string[-1] == '}':
            return checkBraces(string[1:-1])
    return False


def test_checkBraces():
    count = 0
    pass_count = 0
    for test in tests:
        count += 1
        if checkBraces(test[0]) == test[1]:
            pass_count += 1
        else:
            print(f"Fail ({count})")
    print(f"Passed {pass_count} out of {count} tests")


def main():
    test_checkBraces()


if __name__ == "__main__":
    main()
