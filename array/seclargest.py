#native approach sorting 
"""

def seclargest(arr):
    n = len(arr)
    arr.sort
    for i in range(n - 2, -1 , -1):
        if arr[i] != arr[n - 1]:
            return arr[i]

    return -1

if __name__ == "__main__":
    arr = [12,45,13,67,55,67]
    print(seclargest(arr))

"""

#better approach - two pass / one pass 
"""

def twopass(arr):
    n = len(arr)

    largest = -1
    secondlargest = -1

    #one pass
    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]

        elif arr[i] > secondlargest and arr[i] < largest:
            secondlargest = arr[i]

    return secondlargest

"""

    #two pass
def twopass(arr):
    n = len(arr)

    largest = -1
    secondlargest = -1
    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]

    for i in range(n):
        if arr[i] > secondlargest and arr[i] != largest:
            secondlargest = arr[i]

    return secondlargest
   

if __name__ == "__main__":
    arr = [12,34,67,67,56,47]
    print(twopass(arr))

