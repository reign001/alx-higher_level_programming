#!/usr/bin/python3
def print_square(size):
    """
    Prints a square of '#' with the given size.

    Parameters:
    - size (int): The size of the square.

    Returns:
    None
    """
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is greater than or equal to 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Check if size is an integer (not a float) when less than 0
    if size < 0 and not size.is_integer():
         raise TypeError("size must be an integer")

    # Print the square
    for _ in range(size):
        print("# " * size)
