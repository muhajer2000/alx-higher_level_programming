#!/usr/bin/python3
""" module for print squrare characters"""


def text_indentation(text):
    """"" functon that  indentation string by characters
    Arg:
        text : string literal
    return:
        print stinrg with indentation
    Exceptions:
        typeerror: text must be string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        print(char, end='')
        if char == '?' or char == '.':
            print()
            print()
        if char == ':':
            print('')
            print(end='')


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
