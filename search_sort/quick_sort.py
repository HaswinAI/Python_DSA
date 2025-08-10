def quick_sort(arr,low,high):
    if low < high:
        pivot_index = partition(arr,low,high)
        quick_sort(arr,low,pivot_index-1)
        quick_sort(arr,pivot_index+1,high)

def partition(arr,low,high):
    #if choose the last element as pivot
    pivot_index = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot_index:
            i += 1
            arr[i],arr[j] = arr[j], arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

    """
    pivot_index = arr[low]
    # if I using first index then I should use two pointer
    left = low + 1
    right = high
    while True:
        while left <= right and arr[left] <= pivot_index:
            left += 1
        while left <= right and arr[right] >= pivot_index:
            right -= 1
        if left > right:
            break

        arr[left],arr[right] = arr[right],arr[left]
    arr[low],arr[right] = arr[right], arr[low]

    return right
    """

arr = [8,7,6,5,4,3,2,1]
quick_sort(arr,0,len(arr)-1)
print(arr)