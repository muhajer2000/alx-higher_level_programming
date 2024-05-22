def add_integer(a, b=98):
    """" add_intger : function add two intgers 

    Arg:
        a = the first intger
        b = the second intger


    Rasie:
        TypeError: if a, b are not int, float

    Returns:
        The sum of the two integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
        return(a + b)
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
