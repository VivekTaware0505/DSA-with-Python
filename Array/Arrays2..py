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

print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""
Q 07 Move Zeroes to the End

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


print("------------------------------Vivek Learning DSA Python----------------------------------------")

"""
Q .8  Remove Duplicate Elements from sorted Array 

give a sorted array, remove the duplicate element in place without using another array

that means duplicate elements are always next to each other 

e.g. 1 1 2 2 3 4 4
we don't need to search the whole array
we only compare neighboring element

Algorithm We Used

1. Keep i at index 0.

2. Traverse array using j.

3. If nums[i] != nums[j]

      Move i forward.

      Copy nums[j] to nums[i].

4. Continue until end.

5. Return i + 1.

"""


def remove_duplicates(numR):
    if len(numR) == 0:
        return 0
    i = 0

    for j in range (1, len(numR)):

        if numR[i] != numR[j]:
            i += 1

            numR[i] = numR[j]

    return i + 1

numR = [1, 1, 2, 2, 3, 4, 4, 8, 9, 125]    

k = remove_duplicates(numR)

# print(k) to checking list 
print(numR[:k])


print("------------------------------Vivek Learning DSA Python----------------------------------------")