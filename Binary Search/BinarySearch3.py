print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""

Topic : Search in Rotated Sorted Array

🔎 Binary Search — Topic 11: Search in Rotated Sorted Array
This is a very important interview + LeetCode problem and a common advanced Binary Search pattern.
1. What is a Rotated Sorted Array?
First, consider a sorted array:
[0, 1, 2, 4, 5, 6, 7]

If we rotate it around some position:
[4, 5, 6, 7, 0, 1, 2]

This is called a rotated sorted array.
Another example:
Original: [1, 2, 3, 4, 5, 6, 7]

Rotated:  [4, 5, 6, 7, 1, 2, 3]

The array is not completely sorted, but there is an important property:
At least one half of the array is always sorted.

That is the key to solving this in O(log n).
2. The Problem
Given:
arr = [4, 5, 6, 7, 0, 1, 2]
target = 0

Find the index of target.
Answer:
4

If the target doesn't exist:
target = 3

Answer:
-1

3. The Most Important Observation ⭐⭐⭐⭐⭐
Suppose:
arr = [4, 5, 6, 7, 0, 1, 2]
         L     M        R

If:
arr[low] <= arr[mid]

then:
LEFT HALF IS SORTED

For example:
[4, 5, 6, 7]

is sorted.
Otherwise:
RIGHT HALF IS SORTED

For example:
[0, 1, 2]

is sorted.
4. How Do We Decide Which Side to Search?
There are two cases.
Case 1 — Left half is sorted
arr[low] <= arr[mid]

Now check whether target lies inside the sorted left half:
arr[low] <= target < arr[mid]

If yes:
search LEFT

Otherwise:
search RIGHT

Case 2 — Right half is sorted
If:
arr[low] > arr[mid]

then right half is sorted.
Check:
arr[mid] < target <= arr[high]
If yes:
search RIGHT
Otherwise:
search LEFT

"""


print("------------------------------Vivek Learning DSA Python----------------------------------------")





"""


Algorithm To understand


low = 0
high = n - 1

while low <= high:

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid

    if left half is sorted:

        if target lies in left half:
            high = mid - 1
        else:
            low = mid + 1

    else:

        if target lies in right half:
            low = mid + 1
        else:
            high = mid - 1

return -1

"""
def search_rotated(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        # Target found
        if arr[mid] == target:
            return mid

        # Left half is sorted
        if arr[low] <= arr[mid]:

            # Target lies in sorted left half
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # Right half is sorted
        else:

            # Target lies in sorted right half
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


arr = [4, 5, 6, 7, 0, 1, 2]

target = 0

result = search_rotated(arr, target)

print("Index:", result)



print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""

Topic : Find Minimum in Rotated Sorted Array





1. Problem
Given a sorted array that has been rotated, find the minimum element.
Example:
[3, 4, 5, 1, 2]
The original sorted array was:
[1, 2, 3, 4, 5]
After rotation:
[3, 4, 5, 1, 2]
The minimum is:
1
We want to find it in O(log n).
2. Key Observation ⭐⭐⭐⭐⭐
Consider:
[4, 5, 6, 7, 0, 1, 2]
         ↑
       minimum
There are two portions:
[4, 5, 6, 7] [0, 1, 2]
     sorted      sorted
The minimum is where the rotation happens.
The important question is:
Is mid in the left sorted portion or the right sorted portion?

We compare:
arr[mid]
with:
arr[high]

3. The Main Rule 
Case 1
If:
arr[mid] > arr[high]
then the minimum must be to the right of mid.
So:
low = mid + 1
Why?
Example:
[4, 5, 6, 7, 0, 1, 2]
       ↑        ↑
      mid      high

7 > 2
Therefore:
minimum is RIGHT
Case 2
If:
arr[mid] <= arr[high]
then the minimum is at mid or to the left of mid.
So:
high = mid



⚠️ Notice:
high = mid
NOT:
high = mid - 1
because mid itself could be the minimum.
4. Algorithm
low = 0
high = n - 1

while low < high:

    mid = (low + high) // 2

    if arr[mid] > arr[high]:
        low = mid + 1
    else:
        high = mid

return arr[low]

"""


def find_min(arr):
    low = 0
    high = len(arr) - 1

    while low < high:

        mid = (low + high) // 2

        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid

    return arr[low]


arr = [4, 5, 6, 7, 0, 1, 2]

print("Minimum:", find_min(arr))


print("------------------------------Vivek Learning DSA Python----------------------------------------")



"""

The standard problem assumes distinct elements.
If duplicates are allowed, consider:
[2, 2, 2, 0, 1, 2]
Sometimes:
arr[mid] == arr[high]
doesn't tell us which side contains the minimum.
A common modification is:

"""


print("------------------------------Vivek Learning DSA Python----------------------------------------")

"""

Topic :-  find peak element 

1. What is a Peak Element?
A peak element is an element that is greater than its neighboring element(s).
For example:
[1, 3, 5, 4, 2]
       ↑
      5
5 is a peak because:
5 > 3
5 > 4
So the answer is index:
2



2. Important Problem Statement
Given an array where adjacent elements are different, find any peak element and return its index.
Example:
arr = [1, 2, 3, 1]
Peak:
       3
       ↑
[1, 2, 3, 1]
Answer:
2


There can be more than one peak, and returning any one is acceptable.
3. The Important Observation 
This is the trick.
Take:
[1, 2, 7, 4, 3]
       ↑
      mid
At mid, compare:
arr[mid]
with:
arr[mid + 1]
There are two possibilities.
Case 1 — arr[mid] < arr[mid + 1]
Example:
[1, 2, 7, 8, 9, 4]
       ↑  ↑
      mid mid+1
We have:
7 < 8
So we are moving uphill.
That means:
There must be a peak somewhere on the right side.

Therefore:
low = mid + 1
Case 2 — arr[mid] > arr[mid + 1]
Example:
[1, 2, 9, 7, 5, 3]
       ↑  ↑
      mid mid+1
We have:
9 > 7
We are moving downhill.
Therefore a peak exists at mid or somewhere on the left side.
So:
high = mid
Notice again:
high = mid
not:
high = mid - 1
because mid itself might be the peak.

4. The Main Logic 
Memorize this:
arr[mid] < arr[mid + 1]
        ↓
   Peak is RIGHT
        ↓
low = mid + 1
Otherwise:
arr[mid] > arr[mid + 1]
        ↓
Peak is LEFT or MID
        ↓
high = mid
This is the entire core idea.



"""

def find_peak(arr):
    low = 0
    high = len(arr) - 1

    while low < high:

        mid = (low + high) // 2

        if arr[mid] < arr[mid + 1]:
            # We are going uphill
            low = mid + 1

        else:
            # We are going downhill
            high = mid

    return low


arr = [1, 2, 3, 1]

index = find_peak(arr)

print("Peak index:", index)
print("Peak value:", arr[index])

print("------------------------------Vivek Learning DSA Python----------------------------------------")

"""

topic sqaure root using binary search 




1. Problem
Given a number n, find its integer square root without using sqrt().
For example:
√25 = 5
√16 = 4
√10 ≈ 3.16
For 10, the integer square root is:
3
because:
3 × 3 = 9 ≤ 10
4 × 4 = 16 > 10
So we want:
The largest integer x such that x² ≤ n.

2. Why Binary Search?
Suppose:
n = 100
Possible answers are:
0 1 2 3 4 5 6 7 8 9 10
We know:
0² ≤ 100
1² ≤ 100
2² ≤ 100
...
10² ≤ 100
We could check each number one by one:
O(n)
But the answer lies in a sorted numeric range.
Therefore we can Binary Search.
3. Search Space
For:
n = 36
we know:
0 ≤ answer ≤ 36
But we can optimize this.
For n > 1:
answer ≤ n // 2
However, the simplest implementation is:
low = 0
high = n
4. Main Logic 
Calculate:
mid = (low + high) // 2
Then:
mid * mid
Compare it with n.
Case 1
If:
mid * mid == n




Exact square root found.
Return mid.
Case 2
If:
mid * mid < n
mid is too small.
But it might be the answer.
So save it:
answer = mid
and search right:
low = mid + 1
Case 3
If:
mid * mid > n
mid is too large.
Search left:
high = mid - 1


"""


def integer_sqrt(n):
    if n < 2:
        return n

    low = 0
    high = n
    answer = 0

    while low <= high:
        mid = (low + high) // 2

        square = mid * mid

        if square == n:
            return mid

        elif square < n:
            answer = mid
            low = mid + 1

        else:
            high = mid - 1

    return answer


n = 10

print("Integer square root:", integer_sqrt(n))




print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""Optimized Python Version"""


def integer_sqrt(n):
    if n < 2:
        return n

    low = 1
    high = n // 2
    answer = 1

    while low <= high:
        mid = (low + high) // 2

        if mid <= n // mid:
            answer = mid
            low = mid + 1
        else:
            high = mid - 1

    return answer

print("------------------------------Vivek Learning DSA Python----------------------------------------")

"""
Topic : Binary Search on Answer


Normal Binary Search vs Binary Search on Answer
Normal Binary Search
You have:
[10, 20, 30, 40, 50]
and search for:
30
You search among array elements.
Binary Search on Answer
Suppose the answer could be anywhere between:
1 → 100
We don't know the exact answer.
Instead of trying:
1, 2, 3, 4, 5, ...
we use Binary Search:
1 → 50 → 75 → 62 → ...
We repeatedly ask:
Is this candidate answer possible?

This is called a feasibility check.
2. The Most Important Pattern 
Binary Search on Answer generally looks like:
Find possible answer range
          ↓
       low, high
          ↓
        mid
          ↓
 Is mid a valid answer?
      ↙       ↘
    YES        NO
     ↓          ↓
 move one     move other
 direction    direction
The key is that the feasibility condition must be monotonic.
3. What Does Monotonic Mean?
Suppose we test possible answers:
1  2  3  4  5  6  7  8  9  10
N  N  N  N  Y  Y  Y  Y  Y  Y
Here:
N = Not possible
Y = Possible
There is a clear transition:
NOT POSSIBLE → POSSIBLE
Binary Search can find that transition efficiently.
Another pattern can be:
Y Y Y Y N N N N
Both are suitable.
4. Classic Example — Koko Eating Bananas 
This is a famous Binary Search on Answer problem.
Suppose:
piles = [3, 6, 7, 11]
Koko has:
h = 8 hours
She must eat all bananas within 8 hours.
Find the minimum eating speed.
5. What Is the Answer Range?
The slowest possible speed is:
1 banana/hour
The fastest speed we need is:
max(piles)
which is:
11
Therefore:
low = 1
high = 11
Notice:
We are Binary Searching the speed, not the array.

6. Feasibility Check
Suppose speed:
k = 4
For each pile:
3 bananas → 1 hour
6 bananas → 2 hours
7 bananas → 2 hours
11 bananas → 3 hours
Total:
1 + 2 + 2 + 3 = 8 hours
So speed 4 is possible.
7. Formula for Hours
For a pile of p bananas and speed k:
hours = ceil(p / k)
In Python, we can calculate ceiling division using:
(p + k - 1) // k
For example:
(11 + 4 - 1) // 4
gives:
3
"""

def can_finish(piles, h, speed):
    hours = 0

    for bananas in piles:
        hours += (bananas + speed - 1) // speed

    return hours <= h


def min_eating_speed(piles, h):
    low = 1
    high = max(piles)
    answer = high

    while low <= high:
        mid = (low + high) // 2

        if can_finish(piles, h, mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer


piles = [3, 6, 7, 11]
h = 8

print("Minimum speed:", min_eating_speed(piles, h))


print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""

Topic :  Binary Search in 2D matrix 


What is a 2D Matrix?
A matrix is an array containing rows and columns.
Example:
[ 1   3   5   7 ]
[10  11  16  20 ]
[23  30  34  60 ]
It has:
3 rows
4 columns
We can access:
matrix[row][column]
For example:
matrix[1][2]
gives:
16


2. The Problem
Given a matrix where:
1. Every row is sorted.
2. The first element of each row is greater than the last element of the previous row.
Example:
[ 1   3   5   7 ]
[10  11  16  20 ]
[23  30  34  60 ]
Search for:
16
Answer:
Row = 1
Column = 2


3. The Important Observation 
Look at the matrix as if it were a single sorted array.
Matrix:
[ 1   3   5   7 ]
[10  11  16  20 ]
[23  30  34  60 ]
Imagine flattening it:
[1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]
This is sorted.
So instead of doing:
row search
+
column search
we can perform one Binary Search.
4. But We Don't Actually Flatten It
We don't need to create another array.
Suppose:
rows = 3
cols = 4
If Binary Search gives us a virtual index:
mid = 6
we convert it to:
row = mid // cols
column = mid % cols
Therefore:
row = 6 // 4 = 1
column = 6 % 4 = 2
So:
matrix[1][2] = 16

5. The Key Formula 
For a virtual 1D index mid:
In Python:
row = mid // cols
col = mid % cols
This formula is extremely important.


low = 0
high = rows × cols - 1

while low <= high:

    mid = (low + high) // 2

    row = mid // cols
    col = mid % cols

    value = matrix[row][col]

    if value == target:
        return row, col

    elif value < target:
        low = mid + 1

    else:
        high = mid - 1

return -1


"""

def search_matrix(matrix, target):

    rows = len(matrix)
    cols = len(matrix[0])

    low = 0
    high = rows * cols - 1

    while low <= high:

        mid = (low + high) // 2

        row = mid // cols
        col = mid % cols

        value = matrix[row][col]

        if value == target:
            return row, col

        elif value < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]

target = 16

result = search_matrix(matrix, target)

print("Position:", result)


print("------------------------------Vivek Learning DSA Python----------------------------------------")
