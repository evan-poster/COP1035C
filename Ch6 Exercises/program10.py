def myRange(start=None, stop=None):
    """
    Return a list of integers from start to stop.

    Parameters:
        start (int): Starting number, defaults to None.
        stop (int): Ending number, defaults to None.

    Returns:
        list: A list of integers from start to stop.
    """
    result = []

    if start is None and stop is None:
        raise ValueError("Invalid parameters")
    elif start is None:
        start = 0

    if stop is None:
        stop = start
        start = 0

    if start <= stop:
        for i in range(start, stop+1):
            result.append(i)
    else:
        for i in range(start, stop-1, -1):
            result.append(i)

    return result

# Test the myRange function
print(myRange(5))  # [0, 1, 2, 3, 4, 5]
print(myRange(0, 5))  # [0, 1, 2, 3, 4, 5]
print(myRange(5, 0))  # [5, 4, 3, 2, 1, 0]
