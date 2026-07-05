"""Q.06 Given an array of integers, move all 0s to the end while maintaining the relative order of non-zero elements.

first i have crated a new list for this problem
and store all non-zero elements 
count the zeros and also append the zeros at the end 
this is how i look problem 
my name is vivek



"""
def move_zeroes(arr):
    temp = []

    for num in arr:
        if num != 0:
            temp.append(num)

    zero_count = len(arr) - len(temp)

    temp.extend([0] * zero_count)

    return temp

arr = [0,1,0,3,12]
print(move_zeroes(arr))


"""
Move Zeroes to the End

give an array, move all 0s at the end while keeping the order of the non-zero elements the same 

array = 0 1 0 3 12

the all 0s move to end of the line 


we use two pointers 
i - scans every element 
j - points to the position where the next non- zero element should be placed

"""


def move_zeros(nums):
    j=0

    for i in range(len(nums)):
        if nums [i] != 0:
            nums[i], nums[j], nums[i]
            j +=1

    return nums

nums = [ 0, 1, 0, 3, 12]
print(move_zeroes(nums))