"""

Union of two sorted Arrays

Q given two sorted arrays return the union of both arrays 

the union should

contain only unique elements
be in sorted order

Example 1
Input:
arr1 = [1,2,3,4,5]
arr2 = [2,3,4,4,5,6]

Output:
[1,2,3,4,5,6]

Example 2
Input:
arr1 = [1,1,2,3]
arr2 = [2,2,4]

Output:
[1,2,3,4]

put all element into a set
stes automatically remove duplicates 
converts the set back to a list 


"""

def union(arr1, arr2):
    i = 0
    j = 0
    ans = []

    while i < len(arr1) and j < len(arr2):

        if arr1[i] <= arr2[j]:
            if len(ans) == 0 or ans[-1] != arr1[i]:
                ans.append(arr1[i])
            i += 1

        else:
            if len(ans) == 0 or ans[-1] != arr2[j]:
                ans.append(arr2[j])
            j += 1

    while i < len(arr1):
        if ans[-1] != arr1[i]:
            ans.append(arr1[i])
        i += 1

    while j < len(arr2):
        if ans[-1] != arr2[j]:
            ans.append(arr2[j])
        j += 1

    return ans


arr1 = [1,2,3,4,5]
arr2 = [2,3,4,4,5,6]

print(union(arr1, arr2))

print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""
Intersection of two sorted arrays 

Q. Given two sorted arrays return their intersection
the intersection contains only hte common elements
if an element appears multiple times include it only as many as it appears in both arrays



"""

def intersection(arr1, arr2):
    i = 0
    j = 0
    ans = []

    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:
            i += 1

        elif arr1[i] > arr2[j]:
            j += 1

        else:
            ans.append(arr1[i])
            i += 1
            j += 1

    return ans


arr1 = [1,2,2,3,4,5]
arr2 = [2,2,3,5,6]

print(intersection(arr1, arr2))



"""
Q you are given an array containing N-1 numbers

the numbers are from 1 to N only on number id missing
Find the missing number

Input:
arr = [1,2,4,5]

check every number from 1 to N 
if it is not present in the array return it 


"""

def missing_number(arr, n):

    for num in range(1, n + 1):

        if num not in arr:
            return num

arr = [1,2,4,5]

print(missing_number(arr,5))