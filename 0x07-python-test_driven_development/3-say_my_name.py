#!/usr/bin/python3
"""A simple function which prints name"""
def say_my_name(first_name, last_name=""):

    """Prints first name and last name.
    Parameters:
    - first_name: the first name to be entered. Must be a string.
    - last_name: the last name to be entered, must be a string.

    Returns:
    none
    """
    if not (isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if not (isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    print(f"my name is {first_name} {last_name}")
