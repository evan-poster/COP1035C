test_sets = [
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [1, 1, 1, 1, 1],
    [2, 2, 3, 4, 5, 6],
]


def isSorted(lst):
    """Check if a list is sorted"""
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            return False
    return True


if __name__ == "__main__":
    # Iterate through all test sets
    for test_set in test_sets:
        # Inform user if sets are sorted or not
        if isSorted(test_set):
            print(f"{test_set} is sorted")
        else:
            print(f"{test_set} is not sorted")
