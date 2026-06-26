
"""Q.1 Given an array of integers, find the largest element.
 Example
Input:
[10, 5, 20, 8]

Output:
20 

Imagine you are comparing students' marks.

10
5
20
8
 Start by assuming the first number is the largest.

Largest = 10
Compare with every element.

5 > 10 

20 > 10 
Largest = 20

8 > 20 

"""

# program for this problem 

def largest_element(arr):
    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num

    return largest

arr = [10, 5, 20, 8]

print("Largest:", largest_element(arr))

"""
Q.2 Find the minimum element.

Example: we have

Input:
[10,5,20,8]

Output:
5

"""

def smallest_element(arr):
    smallest = arr[0]

    for num in arr:
        if num < smallest:
            smallest = num

    return smallest

arr = [10,5,20,8]

print(smallest_element(arr))