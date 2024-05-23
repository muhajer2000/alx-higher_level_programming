#!/usr/bin/python3
""" module for print squrare characters"""


def print_square(size):
    """"" functon that  print squrare characters
    Arg:
        size : intger number to printed
    return:
        size of characters
    Exceptions:
        typeerror: must be intgers
        valueError : must be grater than 0

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for num in range(size):
        print('#' * size)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
