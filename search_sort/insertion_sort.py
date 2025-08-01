def insertion_sort(arr,n):
    
    for i in range(n):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j - 1

        arr[j+1] = key

arr=[2,5,7,4,9,1]
insertion_sort(arr,len(arr))
print("The sorted array: ",arr)