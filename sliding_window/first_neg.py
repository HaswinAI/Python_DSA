#find first negative in an sub array else return 0
def first_negative(arr,k):
    n = len(arr)
    result = []
    for i in range(n - k + 1):
        found = False
        for j in range(i, i+k):
            if arr[j] < 0:
                result.append(arr[j])
                found = True
                break
            
        if not found:
            result.append(0)

    return result
            

arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
print(first_negative(arr,k))