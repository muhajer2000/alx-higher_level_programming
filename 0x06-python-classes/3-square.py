#!/usr/bin/python3
"""squre module"""


class Square:
    """define """

    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):

        area = self. __size ** 2
        return (area)
