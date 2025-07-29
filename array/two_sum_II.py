def two_sum(arr,target):
    n = len(arr)
    left = 0
    right = n - 1
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            return [left+1,right+1]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return arr



arr = [2,7,8,9,11,15]
target = 9
print(two_sum(arr,target))

            

