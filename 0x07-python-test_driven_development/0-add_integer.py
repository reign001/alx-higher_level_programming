#!/usr/bin/python3
"""defines an integer adding function"""
def add_integer(a, b=98):
        """
        Adds two integers.

        Parameters:
        - a (int or float): The first number.
        - b (int or float): The second number. Defaults to 98.

        Returns:
        int: The sum of a and b.
        """
        """check if a and b are eithr integer or float"""

        if not (isinstance(a,(int, float)) and isinstance(b,(int, float):
                raise TypeError("a must be an integer or b must be an integer")
        """cast a and b to be integers if they are were not"""
                
        a = int(a)
        b = int(b)
        
        return a+b
        
