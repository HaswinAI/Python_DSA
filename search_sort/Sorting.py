def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(i,n-1):
            if arr[i] < arr[j]:
                j = i
        arr[i], arr[j] = arr[j], arr[i]
    return arr
        


arr = [13,46,24,52,20,9]
print(selection_sort(arr))
print(bubble_sort(arr))