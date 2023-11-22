#!/usr/bin/python3

"""efines a class square."""

class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """initializes a new square.
        Args:
        size(int): the size of a new square
        """
        self.size = size
    @property
    def size(self):
        """set/get the size of the current square"""
        return (self.__size)

    @size.setter
    def (self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        """return the current size of the square"""
        return (self.__size * self.__size)
    def my_print(self):
        """prints the square with the # character"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
