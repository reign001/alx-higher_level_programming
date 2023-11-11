#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result_matrix = []
    for row in matrix:
        result_row = []

        for element in row:
            result_row.append(element ** 2)

        answer_matrix.append(result_row)

    return answer_matrix
square_matrix_simple()
