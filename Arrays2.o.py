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