def leader_array(arr):
    result = []
    n = len(arr)

    for i in range(n):
        is_leader = True

        for j in range(i + 1, n):
            if arr[i] < arr[j]:
                is_leader = False
                break
        if is_leader:
            result.append(arr[i])
    return result

arr = [78,98,56,67,43,23,1]
print(leader_array(arr))
