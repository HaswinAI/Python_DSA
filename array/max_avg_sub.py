#sliding window
def max_avg(arr):
    k = 4
    window_sum = sum(arr[:k])/k
    max_sum = window_sum
    for i in range(k,len(arr)):
        window_sum += arr[i] - arr[k-i]
        max_sum = max(window_sum,max_sum)

    return max_sum/k

arr = [1,12,-5,-6,50,3]
print(max_avg(arr))
