def two_sum(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i,n):
            num = arr[i] + arr[j]
            if num == target:
                return i,j 

arr = [2,7,8,12,3]
targer = 9
print(two_sum(arr,target))