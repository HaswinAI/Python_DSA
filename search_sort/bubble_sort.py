def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

def recursive_bsort(arr, n=None):
    if n is None:
        n = len(arr)
    
    if n == 1:
        return
    
    for i in range(n - 1):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1], arr[i]
    
    recursive_bsort(arr, n - 1)

arr = [9,7,3,4,2,3,1]
print(bubble_sort(arr))
recursive_bsort(arr)
print(arr)