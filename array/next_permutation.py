#swapping
"""
def permutation(res,arr,i,j):
    arr[i], arr[j] = arr[j], arr[i]
    res.add(' '.join(arr[:]))
    arr[i], arr[j] = arr[j], arr[i]

def generate(s):
    res = set()
    arr = list(s)

    for i in range(len(arr)):
        for j in range(i + 1,len(arr)):
            permutation(res,arr,i,j)
            
    return len(res)


print(generate("aaaaaaa"))
print(generate("haswinraj"))

"""
#pivot swap

def next_permutation(arr):
    n = arr(len)

    pivot = -1
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i+1]:
            pivoit = i
            break

        if pivot == -1:
            arr.reverse()
            return

        for i in range(n - 1, pivot, -1):
            if arr[i] > arr[pivot]:
                arr[i], arr[pivot] = arr[pivot], arr[i]
                break
        
        left,right = pivot + 1, n - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

arr = [2,4,1,3,5,6,4]
next_permutation(arr)
print(' '.join(map(str,arr)))