
"""

Q.1 given an array of numbers find the next lexicographically greater permutation. if no grater permutation
exist return the smallest (sorted in ascending order )

traverse from the right and find the first indexi where this is the pivot
again from the right find the first element greater than arr[i]
swap them 
reverse th part sfter i 

"""


def next_permutation(nums):
    n = len(nums)

    # Step 1: Find pivot
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    # Step 2: Find next greater element
    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    # Step 3: Reverse suffix
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums


arr = [1, 2, 3]
print(next_permutation(arr))




"""

Q.2 Given an unsorted array, find the length of the longest consecutive sequence.
[100, 4, 200, 1, 3, 2]

A consecutive sequence means numbers that follow each other continuously.

for every number

Search for the next number (x+1)
Then search for (x+2)
Continue until the sequence breaks.


"""

def longest_consecutive(nums):

    num_set = set(nums)
    longest = 0

    for num in num_set:

        if num - 1 not in num_set:

            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


arr = [100,4,200,1,3,2]

print(longest_consecutive(arr))