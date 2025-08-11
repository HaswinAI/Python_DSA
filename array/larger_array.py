def largestElement(nums):
    n = len(nums)
    for i in range(n):
        min_ind = i
        for j in range(i+1,n):
            if nums[j] < nums[min_ind]:
                min_ind = j
            nums[min_ind],nums[i] = nums[i],nums[min_ind]
    return nums[n-1]
            
    

nums = [2,6,9,5,1]
print(largestElement(nums))