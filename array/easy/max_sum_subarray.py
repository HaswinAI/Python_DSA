#brute force (Time limit exceeded)
"""
def max_sum_sub(arr):
    max_sum = 0
    for i in range(0,len(arr)):
        curr_sum = 0
        for j in range(i,len(arr)):
            curr_sum += arr[j]
            max_sum = max(curr_sum,max_sum)
    return max_sum

arr = [5,4,-1,7,8]
print(max_sum_sub(arr))
"""


#divide and conqurie
def max_sub_array(arr):
    if len(arr) == 1:
        return arr[0]
    
    mid = len(arr)//2
    left_max = max_sub_array(arr[:mid])
    right_max = max_sub_array(arr[mid:])
    cross_max = conqurie(arr, mid)
    
    return max(left_max, right_max, cross_max)


def conqurie(arr, mid):
    left_sum = float("-inf")
    curr = 0
    for i in range(mid-1, -1, -1):
        curr += arr[i]
        left_sum = max(left_sum, curr)
    
    right_sum = float("-inf")
    curr = 0
    for i in range(mid, len(arr)):
        curr += arr[i]
        right_sum = max(right_sum, curr)
    
    return left_sum + right_sum

    
    

arr = [5,4,-1,7,8]
print(max_sub_array(arr))