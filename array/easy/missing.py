def missing(arr):
    n = len(arr) + 1
    for i in range(1,n+1):
        if i not in arr:
            return i

arr = [1,2,3,5]
print(missing(arr))