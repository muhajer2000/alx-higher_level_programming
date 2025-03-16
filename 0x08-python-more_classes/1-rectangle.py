#!/usr/bin/python3
""" Class   Rectangle"""

class Rectangle:
    """" create class Rectangle that accept the width of rectangler """
    
    def __init__(self, width = 0, height = 0):
        '''constator method'''
        self.height = height
        self.width = width

    @property
    def width(self):
        """RETUREN FILE FROM THE WIETH FUNCTION , IT IS PROPERTY"""
        return self.__width
    @property
    def height(self):
        """RETURN FILE FROM THE FUNCTION , IT IS PROPERTY"""
        return self.__height
    
    @width.setter
    def width(self, value):
        """ setter method with name vildtion """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """THIS IS SETTER FUNCTION TO SET FROM THE PROPERTY"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


