"""arr = [1,1,4,4,3,3,6,6,7]
unique = []
for i in arr:
    if not unique or i != unique[-1]:
        unique.append(i)

print(unique)"""

def remove_duplicate(arr):
    n = len(arr)
    if n <= 1:
        return n
    
    idx = 1
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            arr[idx] = arr[i]
            idx += 1
    return idx

if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    newSize = remove_duplicate(arr)

    for i in range(newSize):
        print(arr[i], end=" ")