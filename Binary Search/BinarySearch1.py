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






"""


Topic 3 : Recursive Binary Search 

1. What is Recursive Binary Search?

In recursive Binary Search, the function calls itself with a smaller search range.

instead of:

while low <= high:

we repeatedly call:

binary_search(arr, target, low, high)

until:


Basic Idea

Suppose:

[10, 20, 30, 40, 50, 60, 70]

Target:

50

Initially:

low = 0
high = 6

Middle:

mid = 3

arr[3] = 40

Because:

50 > 40

we search the right half:

low = 4
high = 6

The function calls itself again.



The Three Cases
Case 1: Target Found
if arr[mid] == target:
    return mid
Case 2: Target is Smaller
if target < arr[mid]:
    return binary_search(arr, target, low, mid - 1)

Search the left half.

Case 3: Target is Larger
else:
    return binary_search(arr, target, mid + 1, high)

Search the right half.

4. The Most Important Part — Base Case

Every recursive function needs a base case.

Here:

if low > high:
    return -1

This means:

There is no search space left, so the target doesn't exist.

Without a proper base case, recursion could continue indefinitely.

"""

def binary_search(arr, target, low, high):

    if low > high:
        return -1

    mid = low + (high - low) // 2

    if arr[mid] == target:
        return mid

    elif target < arr[mid]:
        return binary_search(arr, target, low, mid - 1)

    else:
        return binary_search(arr, target, mid + 1, high)


arr = [10, 20, 30, 40, 50, 60, 70]
target = 50

result = binary_search(arr, target, 0, len(arr) - 1)

print(result)


print("------------------------------Vivek Learning DSA Python----------------------------------------")



"""


Let's Understand Every Line
Function
def binary_search(arr, target, low, high):

We pass four things:

arr → sorted array
target → value we're searching for
low → beginning of search range
high → end of search range
Base Case
if low > high:
    return -1

If:

low > high

there are no elements remaining.

Find Middle
mid = low + (high - low) // 2
Check Target
if arr[mid] == target:
    return mid

If found, return the index.

Search Left
elif target < arr[mid]:
    return binary_search(arr, target, low, mid - 1)

We don't need the right half.

Search Right
else:
    return binary_search(arr, target, mid + 1, high)

We don't need the left half.

"""



"""



Detailed Dry Run

Array:

[5, 10, 15, 20, 25, 30, 35, 40, 45]

Target:

35
Call 1
low = 0
high = 8

mid = 4

arr[4] = 25

Since:

35 > 25

call:

binary_search(arr, 35, 5, 8)
Call 2
low = 5
high = 8

mid = 6

arr[6] = 35

Found!

return 6

So the answer is:

6
8. Recursion Visualization

The calls look like this:

binary_search(0, 8)
        |
        ↓
binary_search(5, 8)
        |
        ↓
binary_search(5, 5)
        |
        ↓
      Found

Each call reduces the search space.

9. Example Where Target Doesn't Exist

Array:

[10, 20, 30, 40, 50]

Target:

35
Call 1
low = 0
high = 4
mid = 2
arr[2] = 30

35 > 30

low = 3
Call 2
low = 3
high = 4
mid = 3
arr[3] = 40

35 < 40

high = 2

Now:

low = 3
high = 2

Therefore:

low > high

Return:

-1
10. 🟢 Easy Example
arr = [2, 4, 6, 8, 10]
target = 8
result = binary_search(arr, target, 0, len(arr) - 1)

print(result)

Output:

3
11. 🔥 Advanced Example — First Understand the Pattern

Suppose:

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target = 13

The recursive search:

0 → 8

Middle:

4 → 9

13 > 9:

5 → 8

Middle:

6 → 13

🎯 Found at index 6.


12. Iterative vs Recursive Binary Search

This is an important interview question.
Feature	Iterative	Recursive
Uses	Loop	Function calls
Time	O(log n)	O(log n)
Extra Space	O(1)	O(log n)
Stack usage	No	Yes
Performance	Slightly better	Slightly more overhead
Simplicity	Usually simpler	Elegant for recursion practice




Which one should you use?

For practical Python programs:

Iterative Binary Search is generally preferred because it uses O(1) extra space.

Recursive Binary Search is valuable for understanding recursion and for interview questions that specifically ask for a recursive solution.
"""


print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""
Topic Binary Search Templates


1. What is a Binary Search Template?

A template is a standard structure that you can reuse.

Instead of writing Binary Search from zero every time, you remember the basic structure:

low
high
mid
   ↓
compare
   ↓
eliminate half
   ↓
repeat

Most Binary Search interview problems are variations of this idea.


2. The Basic Template

For finding an exact element:

"""
def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1



print("------------------------------Vivek Learning DSA Python----------------------------------------")
