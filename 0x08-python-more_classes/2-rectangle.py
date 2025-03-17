#!/usr/bin/python3
"""Class  Rectangle"""


class Rectangle:
    """
    Rectangle that defines a rectangle by:
    Private instance attribute: width (int)
    Private instance attribute: height (int)
    Instantiation with optional width and height
    Public instance method: def area(self)
    Public instance method: def perimeter(self)
    """
    
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

    def area(self):
        """instante method the return erea of rectangler"""
        return self.width * self.height

    def perimeter(self):
        """instante method that return perimeter of rectangler"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)




