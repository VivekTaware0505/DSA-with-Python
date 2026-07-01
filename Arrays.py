
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



"""
Q.3 Find the second largest number.
track two variables 
"""
def second_largest(arr):

    largest = float('-inf')
    second = float('-inf')

    for num in arr:

        if num > largest:
            second = largest
            largest = num

        elif num > second and num != largest:
            second = num

    return second

arr=[10,5,20,8]

print(second_largest(arr))


"""
Q.4 Reverse an Array

trying to reverse array list using while loop
that print the list in revers 

"""

arr = [1,2,3,4,5]

left = 0
right = len(arr)-1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(arr)

"""
Q.5 Remove Duplicates
"""

arr = [1,2,2,3,4,4]

result = []

for num in arr:
    if num not in result:
        result.append(num)

print(result)

