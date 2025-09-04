def duplicate(arr):
    """
    n = len(arr)
    result = []
    for i in range(n):
        if i == 0 or arr[i] != arr[i - 1]:
            result.append(arr[i])

    return result
    """
    n = len(arr)
    if n <= 1:
        return arr

    idx = 1
    for i in range(1,n):
        if arr[i] != arr[i - 1]:
            arr[idx] = arr[i]
            idx += 1  

    return arr[:idx]

arr = [1,1,2,2,3,3,4,4,5,5]
print(duplicate(arr))