"""

Product of Array Except Self 

Q.1 given an integer array nums, return a new answer such that 

    answer [i] is equal to the product of all element of the array except nums[i]
    
Example
Input:
nums = [1, 2, 3, 4]

Output:
[24, 12, 8, 6]

Now suppose each person wants to know:

"What is the total money contributed by everyone except me?"

For A:

2 × 3 × 4 = 24

For B:

1 × 3 × 4 = 12

For C:

1 × 2 × 4 = 8

For D:

1 × 2 × 3 = 6

So the answer becomes:

[24, 12, 8, 6]

"""

def product_except_self(nums):
    n = len(nums)
    answer = [1] * n

    # Store prefix products
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # Multiply by suffix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer


nums = [2, 3, 4, 5]
print("Output:", product_except_self(nums))


print("------------------------------Vivek Learning DSA Python----------------------------------------")

"""
Longest Consecutive Sequence 

Q.1 you aregiven an unsorted array of integers
you task is to find the length of the longest consecutive sequence 

A consecutive sequence means numbers that come one sfter another 

example:

1, 2, 3, 4, 5

Approach

The best solution uses a Hash Set.

Why Hash Set?

A set allows us to check whether a number exists in O(1) time.

Steps
Store all elements in a set.
Check whether a number is the start of a sequence.
A number is the start if (number - 1) is not in the set.
Keep checking the next consecutive numbers:
number + 1
number + 2
...
Count the length.
Keep the maximum length.


"""

def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Check if it is the start of a sequence
        if num - 1 not in num_set:
            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


nums = [100, 4, 200, 1, 3, 2]
print("Longest Consecutive Length:", longest_consecutive(nums))

print("------------------------------Vivek Learning DSA Python----------------------------------------")
