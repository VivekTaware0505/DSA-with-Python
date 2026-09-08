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
print("------------------------------Vivek Learning DSA Python----------------------------------------")
print("------------------------------Vivek Learning DSA Python----------------------------------------")
print("------------------------------Vivek Learning DSA Python----------------------------------------")
print("------------------------------Vivek Learning DSA Python----------------------------------------")
print("------------------------------Vivek Learning DSA Python----------------------------------------")
print("------------------------------Vivek Learning DSA Python----------------------------------------")
print("------------------------------Vivek Learning DSA Python----------------------------------------")
