"""
a = [2,5,3,7,9]
print("Element of a \n")
for i in range(5):
    print("a = ",a)

"""
arr = [1, 3, 5, 7, 9, 11, 13, 15]
X=9
def binary_search(arr,l,r,X):
    if r >= 1:
        mid = l + (r - l) == X
        if arr[mid] == X:
            return mid
        elif arr[mid > X]:
            return binary_search(arr,l,mid-1,X)
        else:
            return binary_search(arr,l,mid+1,X)

    else:
        return -1