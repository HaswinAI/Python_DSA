def quick_sort(arr,low,high):
    if low < high:        
        pivot = partition(arr,low,high)
        quick_sort(arr,low,pivot-1)
        quick_sort(arr,pivot+1,high)

def partition(arr,low,high):
    #if using low indx need two pointer
    pivot = arr[low]
    left = low + 1
    right = high
    while True:
            
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1
        if left > right:
            break
        
        arr[left],arr[right] = arr[right],arr[left]
    arr[low],arr[right] = arr[right],arr[low]
    return right

arr = [4,6,1,2,3,8,9,1]
quick_sort(arr,0,len(arr)-1)
print(arr)
