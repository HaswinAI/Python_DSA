def reverse_arr(arr):
    n = len(arr)
    left = 0
    right = n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
   

arr = [5,4,3,2,1]
print(reverse_arr(arr))
            