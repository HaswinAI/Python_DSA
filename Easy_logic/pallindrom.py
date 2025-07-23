def pallindome(n):

    s = str(abs(n))
    lenght = len(s)

    for i in range(lenght // 2):
        if s[i] != s[lenght - i - 1]:
            return False
        return True


    """rev = 0
    temp = abs(n)
    while temp != 0:
        last_digit = temp % 10
        rev = rev * 10 + last_digit
        temp //= 10
    return (rev == abs(n))
    """
n = 123432121
if pallindome(n) == True:
    print("Yes")
else:
    print("NO")