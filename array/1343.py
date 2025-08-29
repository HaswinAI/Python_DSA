#number of subarray of size K and avg >= thresehold
def subarray(arr,k,thresehold):
    res = 0
    window_sum = sum(arr[:k])
    for i in range(k,len(arr)):
        window_sum += arr[i] - arr[i-k]
        if (window_sum/k) >= thresehold:
            res += 1

    return res

arr = [2,2,2,2,5,5,5,8]
k = 3
thresehold = 4
print(subarray(arr,k,thresehold))