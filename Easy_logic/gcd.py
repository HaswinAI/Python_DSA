def gcd(a,b):
    while b > 0:
        rem = a % b
        a = b
        b = rem
    return a




print(gcd(12,8))