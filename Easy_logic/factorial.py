def factorial(n):
    
    if n == 0:
        return 1
    return n * factorial(n-1)

    """res = 1
    for i in range(1,n+1):
        res*=i
    return res"""

print(factorial(4))