
def myRange(start, stop=None, step=1):
    """
    Return a list of integers from start to stop.

    Parameters:
        start (int): Starting number, defaults to None.
        stop (int): Ending number, defaults to None.

    Returns:
        list: A list of integers from start to stop.
    """
    if stop is None:
        stop = start
        start = 0

    # Check for errors
    if step == 0:
        return 'Step cannot be zero'
    
    if stop < start and step > 0:
        return 'Stop must be greater than start when step is positive'
    
    if stop > start and step < 0:
        return 'Stop must be less than start when step is negative'
    

    # Create an empty list without the range() function
    result = []
    if step > 0:
        while start < stop:
            result.append(start)
            start += step
    else:
        while start > stop:
            result.append(start)
            start += step
    return result


# Test the myRange function
print(myRange(5))
print(myRange(0, 5))
print(myRange(5, 0))
print(myRange(5, 0, -1))
print(myRange(0, 5, -1))
print(myRange(10, 0, -2))
print(myRange(0, 10, 3))
