"""
Left Rotate an Array by One Position


Q.Given an array, rotate all elements to the left by one position.

so consedring that all alements have the position of right 

and changing the position of all elements 


Store the first element.

Shift every element one position to the left.

Put the stored first element at the last index.

"""


def left_rotate(arr):
    if len(arr) == 0:
        return arr

    temp = arr[0]

    for i in range(len(arr) - 1):
        arr[i] = arr[i + 1]

    arr[-1] = temp
    return arr


arr = [10, 20, 30, 40, 50]

print(left_rotate(arr))

print("------------------------------Vivek Learning DSA Python----------------------------------------")

"""
Q2 Can we rotate without extra space?

we need only one temporary variable 

The array contains only one element.

temp = 1

there are no other element to shift 
place temp back at the last position which is the same position

so array remains the unchanged 


"""

def left_rotate(arr):
    if len(arr) == 0:
        return arr

    temp = arr[0]

    for i in range(len(arr) - 1):
        arr[i] = arr[i + 1]

    arr[-1] = temp

    return arr


arr = [1]

print(left_rotate(arr))

print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""
left rotate an array by K position 

Q 1 give an array and an integer K rotate the array to the left by K position 

every rotation moves the first element to the end 


Method : - Using an Extra Array
store the first K elements
shift the remaining elements to the left
copy the stored elements to the end 

"""

def left_rotate(arr, k):
    n = len(arr)

    k = k % n

    temp = arr[:k]

    arr = arr[k:] + temp

    return arr


arr = [1,2,3,4,5]

print(left_rotate(arr,2))

print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""
Method 2 : - Reversal Alogorithm 

instead of shifting element one by one reverse parts of the array


"""

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def left_rotate(arr, k):
    n = len(arr)

    k = k % n

    reverse(arr, 0, k - 1)

    reverse(arr, k, n - 1)

    reverse(arr, 0, n - 1)

    return arr


arr = [1,2,3,4,5]

print(left_rotate(arr,2))

print("------------------------------Vivek Learning DSA Python----------------------------------------")


