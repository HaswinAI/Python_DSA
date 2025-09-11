
#Kadane algorithm for max sub array
"""
def max_sub_array(nums):
    curr_sum = max_sum = nums[0]
    for i in range(1,len(nums)):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(curr_sum, max_sum)
    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_sub_array(nums))
"""

#sliding window
"""
def sliding_window(arr):
    k = 3
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k,len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum =  max(window_sum,max_sum)
    return max_sum
arr = [2,1,5,1,3,-9,2]
print(sliding_window(arr))
"""