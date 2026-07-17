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



print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""
Spiral Matrix 


Q.1 given an M x N matrix print all the elements in spiral order 



"""
def spiralOrder(matrix):

    result = []

    if not matrix:
        return result

    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    while top <= bottom and left <= right:

        # Left → Right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Top → Bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # Right → Left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # Bottom → Top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(spiralOrder(matrix))


print("------------------------------Vivek Learning DSA Python----------------------------------------")

"""
Pascals Triangle 

generate the first N rows of pascals triangle 




"""

def generate(numRows):
    triangle = []

    for i in range(numRows):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]

        triangle.append(row)

    return triangle


print(generate(5))