"""
Binary Search Algorithm and iterative implementation 

The Core Idea

We have a sorted array:

[10, 20, 30, 40, 50, 60, 70]

Suppose we want to find:

50

We maintain three variables:

low   → beginning of search space
high  → end of search space
mid   → middle position

Initially:

low = 0
high = 6

Calculate:

mid = (low + high) // 2
    = (0 + 6) // 2
    = 3

arr[3] = 40.

Since:

50 > 40

we don't need the left half.

So:

low = mid + 1

Now we search only:

[50, 60, 70]



The Three Possible Cases 
Every iteration has exactly threeimportant possibilities 




3. standard iterative Binary Search 

"""

def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid

        elif target < arr[mid]:
            high = mid - 1

        else:
            low = mid + 1

    return -1


arr = [10, 20, 30, 40, 50, 60, 70]

print(binary_search(arr, 50))

print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""


nderstand Every Line
Line 1
def binary_search(arr, target):

Creates a function that receives:

arr → sorted array
target → element we want to find
Line 2
low = 0

The search starts from the first index.

Line 3
high = len(arr) - 1

high points to the last index.

For:

[10, 20, 30, 40, 50]

the last index is 4.

Line 4
while low <= high:

Continue searching while there is still a valid search range.

Line 5
mid = low + (high - low) // 2

Finds the middle index.

For Python, this is equivalent to:

mid = (low + high) // 2

The first version is commonly preferred in languages where integer overflow can occur.

Lines 6–7
if arr[mid] == target:
    return mid

If the middle element is the target, return its index.

Lines 8–9
elif target < arr[mid]:
    high = mid - 1

Target is smaller → move high to the left.

Lines 10–11
else:
    low = mid + 1

Target is larger → move low to the right.

Final
return -1

If the loop finishes without finding the target, return -1.

5. Detailed Dry Run 🔥

Array:

[5, 10, 15, 20, 25, 30, 35, 40, 45]

Target:

35
Step 1
low = 0
high = 8

mid = (0 + 8) // 2
    = 4

Middle:

arr[4] = 25

Compare:

35 > 25

Therefore:

low = mid + 1
low = 5
Step 2
low = 5
high = 8

mid = (5 + 8) // 2
    = 6

Middle:

arr[6] = 35

Compare:

35 == 35

🎯 Found!

Answer:

6
6. What Happens When the Element Doesn't Exist?

Array:

[10, 20, 30, 40, 50]

Target:

35

The search eventually reaches:

low > high

There is no search space left.

Therefore:

return -1

Output:

-1
7. Example With a Small Array
arr = [2, 4, 6, 8, 10]
target = 8
Dry Run
low = 0
high = 4

mid = 2

arr[2] = 6

Since:

8 > 6

move right:

low = 3

Now:

low = 3
high = 4

mid = 3
arr[3] = 8

Found.

Output:

3





"""
print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""
Q.1 find the target in a sorted array 



[3, 8, 12, 17, 25, 31, 42, 56, 71, 90]

Target:

71

"""

def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid

        if target < arr[mid]:
            high = mid - 1

        else:
            low = mid + 1

    return -1


arr = [3, 8, 12, 17, 25, 31, 42, 56, 71, 90]

print(binary_search(arr, 71))

print("------------------------------Vivek Learning DSA Python----------------------------------------")
"""

Important Interview Variation

Instead of returning the index, return:

True → element exists
False → element doesn't exist


"""


def contains(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] == target:
            return True

        elif target < arr[mid]:
            high = mid - 1

        else:
            low = mid + 1

    return False


arr = [10, 20, 30, 40, 50]

print(contains(arr, 40))
print(contains(arr, 45))
print("------------------------------Vivek Learning DSA Python----------------------------------------")
