def sec_largest(arr):
    n = len(arr)

    if len(arr) < 2:
        return -1
    
    largest = -1
    second_largest = -1

    for i in range(n):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        
        elif arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]

    return second_largest

arr = [-5,-10,10,2,4,9]

print(sec_largest(arr))