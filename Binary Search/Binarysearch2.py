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
print("------------------------------Vivek Learning DSA Python----------------------------------------")
