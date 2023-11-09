#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    answer_matrix = []
    for row in matrix:
        answer_row = []

        for element in row:
            answer_row.append(element ** 2)

        answer_matrix.append(result_row)

    return answer_matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

answer = square_matrix_simple(matrix)
print(answer)
