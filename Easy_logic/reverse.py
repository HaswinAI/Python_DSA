def reverse(n):

    """
    is_negative = n > 0
    n = abs(n)
    s = str(n)
    ch = s[::-1]
    n = int(ch)
    return -n if is_negative else n

    """    
    is_negative = n < 0
    n = abs(n)
    rev = 0
    while n != 0:
        last_digit = n % 10
        rev = rev * 10 + last_digit
        n = n // 10
        
    return -rev if is_negative else rev
    
print(reverse(12345))
print(reverse(-12345))