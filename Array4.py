
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