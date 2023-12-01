def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a divisor.

    Parameters:
    - matrix (list of lists): The matrix to be divided. Must contain only integers or floats.
    - div (int or float): The divisor.

    Returns:
    list of lists: A new matrix with elements divided by the divisor, rounded to 2 decimal places.
    """
    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) and all(isinstance(element, (int, float)) for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero is not allowed")

    # Perform matrix division and rounding
    result_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return result_matrix
