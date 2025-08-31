def larger_element(arr):
    
    #basecase
    if len(arr) == 1:
        return arr[0]

    rest_max = larger_element(arr[1:])
    return arr[0] if arr[0] > rest_max else rest_max
        
    
    

arr = [0,1,9,2,3,4,5,8,1,0]
print(larger_element(arr))    