#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for k in range(len(matrix)):
        new_matrix[k] = list(map(lambda y: x**2, matrix[i]))
    return (new_matrix)
