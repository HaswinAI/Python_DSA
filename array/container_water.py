#two pointer opposit left --> <-- right
def container(arr):
    left = 0
    right = len(arr) - 1
    max_water = 0
    while left < right:
        width = right - left
        height  = min(arr[left], arr[right])
        water = width * height
        max_water = max(max_water, water)
            
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    return max_water
            

#brute force method for contaner water
"""
def container(arr):
    n = len(arr)
    max_water = 0
    for i in range(n):
        for j in range(i + 1, n):
            water = (j-i) * min(arr[i],arr[j])
            max_water = max(max_water,water)

    return max_water
"""
arr = [1,8,6,2,5,4,8,3,7]
print(container(arr))