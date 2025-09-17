def right_rotate(arr,k):
    n = len(arr)
    temp = arr[n-1]
    for i in range(n-k):
        arr[i] = arr[i+1]
        arr[n-1] = temp
    return arr

arr = [1,2,3,4,5,6,7]
k = 2
print(right_rotate(arr,k))