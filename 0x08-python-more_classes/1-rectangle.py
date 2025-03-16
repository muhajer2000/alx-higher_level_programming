#!/usr/bin/python3
""" Class   Rectangle"""

class Rectangle:
    """" create class Rectangle that accept the width of rectangler """
    
    def __init__(self, width = 0, height = 0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """RETUREN FILE FROM THE WIETH FUNCTION , IT IS PROPERTY"""
        return self.__width

    @width.setter
    def width(self, value):
        """ setter method with name vildtion """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """RETURN FILE FROM THE FUNCTION , IT IS PROPERTY"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """THIS IS SETTER FUNCTION TO SET FROM THE PROPERTY"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)
