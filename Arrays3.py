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