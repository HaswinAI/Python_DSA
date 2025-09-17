def move_zero(arr):
    #optimal
    n = len(arr)
    count = 0
    for i in range(n):
        if arr[i] != 0:
            arr[i],arr[count] = arr[count],arr[i]
            count += 1

    return arr


    #brute force
    """
    n = len(arr)
    temp = []
    for i in range(n):
        if arr[i] != 0:
            temp.append(arr[i])
    
    zero = n - len(temp)

    for _ in range(zero):
        temp.append(0)
    return temp
    """

arr = [1,0,2,0,3,0,4,5,0]
print(move_zero(arr))