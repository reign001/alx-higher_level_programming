#!/usr/bin/python3

"""defines a class square"""

class Square:

    """Represents a square"""

    def __init__(self, size=0):
        
        """initializes a square.
        Args:
            size(int)the size of the new square
        """

        if not ininstance(size, int):
            raise TypeError(("size must be an integer")
        elif size <0:
            raise ValueError("size must be >=0")
        self.size = size

    def area(self):

        """return the current area of the square"""

        return (self.__size * self.__size)
