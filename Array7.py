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


"""

Container with Most Water 

Q.1 you are given an array height [], where each element represent the height of a vertical line
Choose any two lines so that together with the x-axis they from a container 
your task is to find the maximum amount of water that the container can store 

Example
Input:
height = [1,8,6,2,5,4,8,3,7]

Output:
49


Approach

We use the Two Pointer Technique.

Steps
Place one pointer at the left end.
Place another pointer at the right end.
Calculate the current area.
Update the maximum area.
Move the pointer with the smaller height inward.
Repeat until the pointers meet.
Why move the smaller height?

The shorter line limits the water. Moving the taller line cannot increase the height limit, 
but moving the shorter line may find a taller line and increase the area.

"""

def max_area(height):
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        area = min(height[left], height[right]) * width
        max_water = max(max_water, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


height = [1,8,6,2,5,4,8,3,7]
print("Maximum Water:", max_area(height))


print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""

Trapping Rain Water

Q.1 you are given an array height[], where each element represent the height of a building 
after it rains, water gets trapped between the buildings 
your task is to calculate the total amount of rainwater trapped 

Example
Input:
height = [0,1,0,2,1,0,1,3,2,1,2,1]

Output:
6

Key Idea

Water can only be trapped if there is:

A taller building on the left.
A taller building on the right.

The water level above a building is:

Water = min(Max Left Height, Max Right Height) - Current Height

If this value is negative, treat it as 0.

Approach (Two Pointer - Optimal)

We use two pointers:

left = 0
right = n - 1

Also maintain:

left_max
right_max
Steps
Compare height[left] and height[right].
Move the side with the smaller height.
Update the maximum height seen so far.
If the current height is smaller than the maximum, water is trapped.
Add trapped water to the answer.
Continue until left meets right.

"""

def trap(height):
    left = 0
    right = len(height) - 1

    left_max = 0
    right_max = 0
    water = 0

    while left < right:

        if height[left] < height[right]:

            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]

            left += 1

        else:

            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]

            right -= 1

    return water


height = [3,0,2,0,4]
print("Water Trapped:", trap(height))