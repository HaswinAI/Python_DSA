def leader_array(arr):
    result =[]
    max_right = arr[-1]
    result.append(max_right)

    for i in range(len(arr)-2, -1, -1):
        if arr[i] >= max_right:
            result.append(arr[i])
            max_right = arr[i]

    return result[::-1]


    """result = []
    n = len(arr)

    for i in range(n):
        is_leader = True

        for j in range(i + 1, n):
            if arr[i] < arr[j]:
                is_leader = False
                break
        if is_leader:
            result.append(arr[i])
    return result"""

arr = [78,98,56,67,43,23,1]
print(leader_array(arr))
