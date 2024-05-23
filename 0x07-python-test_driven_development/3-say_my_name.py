#!/usr/bin/python3
""" module for say my name"""


def say_my_name(first_name, last_name=""):
    """"" functon that print first and last name
    Arg:
        first_name: first name
        lasr_name: last name
    return 
        print first and last name 
    Exceptions:
        typeerror: must be string
        typeError : mustbestring
    
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
