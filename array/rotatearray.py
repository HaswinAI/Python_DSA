def rotatearray(arr,d):
    n = len(arr)

    for j in range(d):
        
        first = arr[0]
        for k in range(n-1):
            arr[k] = arr[k+1]
        arr[n-1] = first


if __name__=="__main__":
    arr = [1,2,3,4,5,6,7]
    d = 3
    rotatearray(arr,d)

    for i in range(len(arr)):
        print(arr[i],end=" ")