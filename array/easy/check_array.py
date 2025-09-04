def check(arr):
    n = len(arr)
    
    for i in range(1,n):
        if arr[i] < arr[i-1]:
            return False
    return True


arr = [1,2,3,5,4,6]
print(check(arr))   