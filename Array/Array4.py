
"""

Q.1 given an array of numbers find the next lexicographically greater permutation. if no grater permutation
exist return the smallest (sorted in ascending order )

traverse from the right and find the first indexi where this is the pivot
again from the right find the first element greater than arr[i]
swap them 
reverse th part sfter i 

"""


def next_permutation(nums):
    n = len(nums)

    # Step 1: Find pivot
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    # Step 2: Find next greater element
    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    # Step 3: Reverse suffix
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums


arr = [1, 2, 3]
print(next_permutation(arr))


print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""

Q.2 Given an unsorted array, find the length of the longest consecutive sequence.
[100, 4, 200, 1, 3, 2]

A consecutive sequence means numbers that follow each other continuously.

for every number

Search for the next number (x+1)
Then search for (x+2)
Continue until the sequence breaks.


"""

def longest_consecutive(nums):

    num_set = set(nums)
    longest = 0

    for num in num_set:

        if num - 1 not in num_set:

            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


arr = [100,4,200,1,3,2]

print(longest_consecutive(arr))

print("------------------------------Vivek Learning DSA Python----------------------------------------")



"""

set Matrix Zeros 

Q.1 given an m x n matrix if an element is 0 set is entire row and column to 0

Make the whole row zero.
Make the whole column zero.
"""

def set_zeroes(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    row = [False] * rows
    col = [False] * cols

    # Mark rows and columns
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                row[i] = True
                col[j] = True

    # Update matrix
    for i in range(rows):
        for j in range(cols):
            if row[i] or col[j]:
                matrix[i][j] = 0

    return matrix


matrix = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
]

print(set_zeroes(matrix))

print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""
Optimal Approach (interview favorite )
instead of using two extra arrays

first row first column as array makers 

python program 


"""

def setZeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    first_col = False

    # Mark rows and columns
    for i in range(rows):
        if matrix[i][0] == 0:
            first_col = True

        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Fill zeroes
    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, 0, -1):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

        if first_col:
            matrix[i][0] = 0

    return matrix


matrix = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
]

print(setZeroes(matrix))


print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""
Common Interview Questions
Q1. Why can't we directly make rows and columns zero?

Because newly created zeroes would incorrectly influence other rows and columns.

Q2. Why traverse from bottom-right in the optimal solution?

To avoid overwriting the marker information in the first row and first column before it's fully used.

Q3. Which solution should you explain first?

Start with:

Brute Force
Better (O(m+n) space)
Optimal (O(1) space)

This demonstrates your problem-solving and optimization skills.

"""
