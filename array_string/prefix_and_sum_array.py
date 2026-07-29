
"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation."""

def prefix_and_sum_solution(arr:list):

    length_arr=len(arr)
    prefix=[0]*length_arr

    prefix[0]=arr[0]
    for i in range(1,length_arr):
        prefix[i]=prefix[i-1]*arr[i]

    suffix=1
    for i in range(length_arr-1,0,-1):
        prefix[i]=prefix[i-1]*suffix
        suffix*= arr[i]

    prefix[0]=suffix
    return prefix


print(prefix_and_sum_solution([1,2,3,4]))