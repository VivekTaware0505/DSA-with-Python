"""
Rotate Matrix by 90degree (clockwise)

Q. 1 Given an N × N matrix, rotate it 90° clockwise without using extra space.
Instead of creating another matrix:

Transpose the matrix.
Reverse each row.

This is the most common interview solution.

"""

def rotate(matrix):
    n = len(matrix)

    # Step 1: Transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()

    return matrix


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(rotate(matrix))