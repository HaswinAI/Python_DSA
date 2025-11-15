def largest(arr):
    n = len(arr)
    for i in range(n):
        arr.sort()
    return arr
    
arr = [5,8,1,2,4,3]
print(largest(arr))
