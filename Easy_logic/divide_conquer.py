def min_max_divide_conquer(arr):
    def helper(left, right):
        if left == right:
            return arr[left], arr[right]
        
        if right == left + 1:
            return min(arr[left], arr[right]), max(arr[left], arr[right])
        
        mid = (left + right) // 2

        #conquer - recuresive call
        left_min, left_max = helper(left,mid)
        right_min, right_max = helper(mid+1,right)

        return min(left_min, right_min), max(left_max, right_max)
    
    return helper(0,len(arr)-1)

print(min_max_divide_conquer([3,4,5,1,9]))

