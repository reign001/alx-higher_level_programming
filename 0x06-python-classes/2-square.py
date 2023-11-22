#!/usr/bin/python3

"""defines a class square"""
class Square:
    """represents a square"""
    def __init__(self, size=0):
        """initializes a new square.
        Args:
            size(int): the size of a new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
