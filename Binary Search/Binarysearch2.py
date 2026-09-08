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
print("------------------------------Vivek Learning DSA Python----------------------------------------")
print("------------------------------Vivek Learning DSA Python----------------------------------------")
print("------------------------------Vivek Learning DSA Python----------------------------------------")
print("------------------------------Vivek Learning DSA Python----------------------------------------")
print("------------------------------Vivek Learning DSA Python----------------------------------------")
