
def summation(lower, upper):
    result = 0
    while lower <= upper:
        result += lower
        lower += 1
    return result


def r_summation(lower, upper):
    if lower > upper:
        return 0
    return lower + r_summation(lower + 1, upper)


if __name__ == "__main__":
    print(summation(1,5))
    print(r_summation(1,5))
