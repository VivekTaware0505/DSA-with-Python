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

print("------------------------------Vivek Learning DSA Python----------------------------------------")

"""

Merge Overlapping Intervals

Q.1 you are given an array of intervels where each interval is represented as 

[start, end]

If two intervals overlap, merge them into a single interval.

Return all merged intervals.

Example 1
intervals = [[1,3],[2,6],[8,10],[15,18]]

Current=[1,3]

↓

Merge

↓

Current=[1,6]

↓

Store

↓

[8,10]

↓

Store

↓

[15,18]




"""

def merge(intervals):

    intervals.sort()

    result = [intervals[0]]

    for start, end in intervals[1:]:

        last_end = result[-1][1]

        if start <= last_end:

            result[-1][1] = max(last_end, end)

        else:

            result.append([start, end])

    return result


intervals = [[1,3],[2,6],[8,10],[15,18]]

print(merge(intervals))

print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""

Insert Interval

you are given a list of non overlapping intervals sorted by start time and a new interval
insert the new interval into the correct position and merge if necessary 

Example 1
intervals = [[1,3],[6,9]]
newInterval = [2,5]

"""
def insert(intervals, newInterval):

    result = []

    i = 0
    n = len(intervals)

    # Step 1: Add intervals before newInterval
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Step 2: Merge overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    # Step 3: Add merged interval
    result.append(newInterval)

    # Step 4: Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result


intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

print(insert(intervals, newInterval))


print("------------------------------Vivek Learning DSA Python----------------------------------------")



"""

Next Permutation

Q .1 Given an array representing a permutation of numbers, rearrange it into the next lexicographically greater permutation.

If no greater permutation exists (i.e., it's already the largest), rearrange it to the smallest possible order (ascending).

The modification must be in-place (without using extra space).

Example 1
nums = [1,2,3]

Output

[1,3,2]

Because:

123
132   ← Next greater permutation
213
231
312
321
Example 2
nums = [3,2,1]

Output

[1,2,3]

Reason:

321

is already the largest permutation, so return the smallest.

Example 3
nums = [1,1,5]

Output

[1,5,1]
What is Lexicographical Order?

It is dictionary order.

Example:

123
132
213
231
312
321

Each next number is the next permutation.

"""


def nextPermutation(nums):

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
    left = i + 1
    right = n - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


nums = [1,2,3]

nextPermutation(nums)

print(nums)