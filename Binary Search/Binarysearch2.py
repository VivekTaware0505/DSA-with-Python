"""

Topic : Upper Bound 


1. What is Upper Bound?
In simple language:
Upper Bound finds the first index where arr[index] > target.

Notice the difference:
Lower Bound
arr[i] >= target
Upper Bound
arr[i] > target
2. Simple Example
Consider:
Array = [1, 3, 3, 3, 5, 7]
Target = 3
Lower Bound
First element >= 3:
index 1 → 3
So:
Lower Bound = 1
Upper Bound
First element > 3:
index 4 → 5
So:
Upper Bound = 4
Remember
[1, 3, 3, 3, 5, 7]
    ↑       ↑
   LB      UB
    1       4
3. The Main Difference
	Lower Bound	Upper Bound
Condition	arr[i] >= target	arr[i] > target
Finds	First ≥ target	First > target
If target exists	First occurrence	Position after last occurrence
Complexity	O(log n)	O(log n)


This one-character difference is extremely important:
Lower Bound → >=
Upper Bound → >
4. Upper Bound Logic
We use:
low = 0
high = len(arr) - 1
answer = len(arr)
Then:
while low <= high:
Calculate:
mid = low + (high - low) // 2
Now the key decision:
If:
arr[mid] > target
We've found a possible answer.
Save it:
answer = mid
But maybe there is another value greater than the target further left.
So:
high = mid - 1
Otherwise:
arr[mid] <= target
The current value isn't greater than the target.
We must go right:
low = mid + 1


"""

def upper_bound(arr, target):

    low = 0
    high = len(arr) - 1
    answer = len(arr)

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] > target:
            answer = mid
            high = mid - 1

        else:
            low = mid + 1

    return answer


arr = [1, 3, 3, 3, 5, 7]

print(upper_bound(arr, 3))


print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""




Problem
Given:
arr = [2, 4, 4, 4, 4, 6, 8, 10]
Find the Upper Bound of:
4
We need:
first element > 4
That's:
6
at index:
5


"""

def upper_bound(arr, target):

    low = 0
    high = len(arr) - 1
    answer = len(arr)

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] > target:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer


arr = [2, 4, 4, 4, 4, 6, 8, 10]

result = upper_bound(arr, 4)

print(result)




print("------------------------------Vivek Learning DSA Python----------------------------------------")

"""


UPPER BOUND

Definition:
First index where arr[i] > target.

If arr[mid] > target:
    answer = mid
    high = mid - 1

If arr[mid] <= target:
    low = mid + 1

Initial answer:
    len(arr)

Time:
    O(log n)

Space:
    O(1)



"""
print("------------------------------Vivek Learning DSA Python----------------------------------------")



"""

Topic : Floor and Celi




1. What is Floor?
The Floor of a target is:
The largest element that is less than or equal to the target.

Mathematically:
Example
arr = [1, 3, 5, 7, 9]
target = 6
Values ≤ 6:
1, 3, 5
Largest = 5
Therefore:
Floor = 5
2. What is Ceil?
The Ceil of a target is:
The smallest element that is greater than or equal to the target.

Example:
arr = [1, 3, 5, 7, 9]
target = 6
Values ≥ 6:
7, 9
Smallest = 7
Therefore:
Ceil = 7
3. Easy Way to Remember
For:
arr = [1, 3, 5, 7, 9]
target = 6
       Floor   Target   Ceil
          ↓       ↓       ↓
[1, 3, 5, 7, 9]
       5       6       7
Remember:
Floor → goes DOWN
Ceil → goes UP
4. Floor Using Binary Search
We need:
largest element <= target
Logic
If:
arr[mid] <= target
then arr[mid] is a possible Floor.
Save it:
answer = arr[mid]
But maybe there is a larger valid value.
So go right:
low = mid + 1
If:
arr[mid] > target
the value is too large.
Go left:
high = mid - 1





"""
def find_floor(arr, target):

    low = 0
    high = len(arr) - 1
    answer = None

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] <= target:
            answer = arr[mid]
            low = mid + 1

        else:
            high = mid - 1

    return answer


arr = [1, 3, 5, 7, 9]

print(find_floor(arr, 6))


print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""

Ceil Using Binary Search
Now we need:
smallest element >= target
If:
arr[mid] >= target
we found a possible Ceil.
Save it:
answer = arr[mid]
But maybe there is a smaller valid value.
So go left:
high = mid - 1
Otherwise:
arr[mid] < target
The value is too small.
Go right:
low = mid + 1


"""


def find_ceil(arr, target):

    low = 0
    high = len(arr) - 1
    answer = None

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] >= target:
            answer = arr[mid]
            high = mid - 1

        else:
            low = mid + 1

    return answer


arr = [1, 3, 5, 7, 9]

print(find_ceil(arr, 6))
print("------------------------------Vivek Learning DSA Python----------------------------------------")




"""

This is the Version i'd recommend you understand well for interviews 

"""



def floor_ceil(arr, target):

    low = 0
    high = len(arr) - 1

    floor = None
    ceil = None

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] == target:
            return arr[mid], arr[mid]

        elif arr[mid] < target:
            floor = arr[mid]
            low = mid + 1

        else:
            ceil = arr[mid]
            high = mid - 1

    return floor, ceil


arr = [1, 3, 5, 7, 9]

floor, ceil = floor_ceil(arr, 6)

print("Floor:", floor)
print("Ceil:", ceil)




print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""


Topic : First and Last Occurrence



The Problem
Suppose we have:
arr = [1, 2, 2, 2, 2, 5, 7]
Target:
2
We want:
First occurrence → 1
Last occurrence  → 4
Visual:
Index:   0  1  2  3  4  5  6
Array:   1  2  2  2  2  5  7
            ↑           ↑
          First        Last
2. Why Normal Binary Search Isn't Enough
Normal Binary Search might find:
index = 3
That's a valid occurrence.
But the question asks specifically for:
First → index 1
Last  → index 4
So we need to modify Binary Search.
3. Finding First Occurrence
The easiest way is to use the Lower Bound idea.
We want:
first arr[i] >= target
For:
[1, 2, 2, 2, 2, 5, 7]
target = 2
Lower Bound gives:
1
Since:
arr[1] == target
the first occurrence is:
1
Important:
Lower Bound can return the insertion position even if the target doesn't exist.
So we must verify:
if index < len(arr) and arr[index] == target:

"""

def first_occurrence(arr, target):

    low = 0
    high = len(arr) - 1
    answer = -1

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] >= target:
            answer = mid
            high = mid - 1

        else:
            low = mid + 1

    if answer != -1 and arr[answer] == target:
        return answer

    return -1


arr = [1, 2, 2, 2, 2, 5, 7]

print(first_occurrence(arr, 2))





print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""

Finding Last Occurrence 



Now we use the Upper Bound idea.
Upper Bound gives:
First index where arr[i] > target.

For:
[1, 2, 2, 2, 2, 5, 7]
target = 2
Upper Bound:
5
Index 5 contains 5.
Therefore:
Last occurrence = Upper Bound - 1
So:
5 - 1 = 4
Answer:
4
"""




def last_occurrence(arr, target):

    low = 0
    high = len(arr) - 1
    answer = -1

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] > target:
            high = mid - 1

        else:
            answer = mid
            low = mid + 1

    if answer != -1 and arr[answer] == target:
        return answer

    return -1


arr = [1, 2, 2, 2, 2, 5, 7]

print(last_occurrence(arr, 2))
print("------------------------------Vivek Learning DSA Python----------------------------------------")

"""

First Occurrence and last Occurrence example 

"""


def first_occurrence(arr, target):

    low = 0
    high = len(arr) - 1
    answer = -1

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] >= target:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    if answer != -1 and arr[answer] == target:
        return answer

    return -1


def last_occurrence(arr, target):

    low = 0
    high = len(arr) - 1
    answer = -1

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] > target:
            high = mid - 1
        else:
            answer = mid
            low = mid + 1

    if answer != -1 and arr[answer] == target:
        return answer

    return -1


arr = [1, 2, 2, 2, 2, 5, 7]
target = 2

first = first_occurrence(arr, target)
last = last_occurrence(arr, target)

print("First occurrence:", first)
print("Last occurrence:", last)
print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""
Complete Frequency Program

"""

def first_occurrence(arr, target):

    low = 0
    high = len(arr) - 1
    answer = -1

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] >= target:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    if answer != -1 and arr[answer] == target:
        return answer

    return -1


def last_occurrence(arr, target):

    low = 0
    high = len(arr) - 1
    answer = -1

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] <= target:
            answer = mid
            low = mid + 1
        else:
            high = mid - 1

    if answer != -1 and arr[answer] == target:
        return answer

    return -1


def count_occurrences(arr, target):

    first = first_occurrence(arr, target)

    if first == -1:
        return 0

    last = last_occurrence(arr, target)

    return last - first + 1


arr = [1, 2, 2, 2, 2, 5, 7]

print(count_occurrences(arr, 2))
print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""

Topic ; Count Occurrence 


In a sorted array, count how many times a target appears using Binary Search instead of scanning the whole array.

1. Example
arr = [1, 2, 2, 2, 2, 5, 7]
target = 2
We know:
First occurrence = 1
Last occurrence  = 4
So the number of occurrences is:
= 4 - 1 + 1
= 4
Answer: 4
2. Best Binary Search Formula 
There is an even cleaner method using Lower Bound and Upper Bound:
For:
[1, 2, 2, 2, 2, 5, 7]
Target = 2
Lower Bound = 1
Upper Bound = 5
Therefore:
Count = 5 - 1
      = 4
3. Why Does This Work?
Look at the array:
Index:   0  1  2  3  4  5  6
Array:   1  2  2  2  2  5  7
            ↑           ↑
           LB          UB
            1           5
The target occupies indices:
1, 2, 3, 4
Number of positions:
5 - 1 = 4
That's the beauty of Lower/Upper Bound.



"""


def lower_bound(arr, target):

    low = 0
    high = len(arr)

    while low < high:

        mid = low + (high - low) // 2

        if arr[mid] >= target:
            high = mid
        else:
            low = mid + 1

    return low


def upper_bound(arr, target):

    low = 0
    high = len(arr)

    while low < high:

        mid = low + (high - low) // 2

        if arr[mid] > target:
            high = mid
        else:
            low = mid + 1

    return low


def count_occurrences(arr, target):

    first = lower_bound(arr, target)
    last = upper_bound(arr, target)

    return last - first


arr = [1, 2, 2, 2, 2, 5, 7]

print(count_occurrences(arr, 2))

print("------------------------------Vivek Learning DSA Python----------------------------------------")
print("------------------------------Vivek Learning DSA Python----------------------------------------")


