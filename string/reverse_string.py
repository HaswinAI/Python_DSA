def reverse_string(str):
    n = len(str)
    left = 0
    right = n - 1
    while left < right:
        str[left], str[right] = str[right],str[left]
        left += 1
        right -= 1
    return str
    

str = ["H","E","L","L","O"]
print(reverse_string(str))
