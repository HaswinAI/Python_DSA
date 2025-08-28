def largestElement(nums, i=0, max_value=None):
    #using bubble recursive sort
    if max_value is None:
        max_value = nums[0]
    
    if i == len(nums):
        return max_value

    if nums[i] > max_value:
        max_value = nums[i]

    return largestElement(nums, i+1, max_value)
        

    """
    n = len(nums)
    for i in range(n):
        min_ind = i
        for j in range(i+1,n):
            if nums[j] < nums[min_ind]:
                min_ind = j
            nums[min_ind],nums[i] = nums[i],nums[min_ind]
    return nums[n-1]
    """
    

nums = [3, 7, 2, 9, 5]
print(largestElement(nums))
+