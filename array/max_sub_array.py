#Kadane algorithm for max sub array
def max_sub_array(nums):
    curr_sum = max_sum = nums[0]
    for i in range(1,len(nums)):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(curr_sum, max_sum)
    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_sub_array(nums))