#brute froce
"""
def majority_element(arr):
    n = len(arr)
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[j] == arr[i]:
                count += 1

        if count > n // 2:
            return arr[i]

    return -1
"""

def hashmap(arr):
    freq = {}
    n = len(arr)
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

        if num > n // 3 :
            return num 
    return -1


arr=[2,2,1,2,2,2,3]
print(hashmap(arr))