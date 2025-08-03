def reverse_bit(x):
    negative = x < 0
    x = abs(x)
    rev = 0
    while x != 0:
        last_digit = x % 10
        rev = rev * 10 + last_digit
        x = x // 10    
    if negative:
        rev = -rev

    if rev < -2**31 or rev > 2**31:
        return 0
    return rev

print(reverse_bit(-123))