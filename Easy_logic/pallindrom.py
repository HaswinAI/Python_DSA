def pallindome(n):
    n = str(n)
    #two pointer opposite
    left, right = 0, len(n) - 1
    while left < right:
        if n[left] != n[right]:
            return False
        left +=1
        right -=1
    return True

    """
    s = str(abs(n))
    lenght = len(s)

    for i in range(lenght // 2):
        if s[i] != s[lenght - i - 1]:
            return False
        return True
    """

    """rev = 0
    temp = abs(n)
    while temp != 0:
        last_digit = temp % 10
        rev = rev * 10 + last_digit
        temp //= 10
    return (rev == abs(n))
    """
n = 122222421
if pallindome(n) == True:
    print("Yes")
else:
    print("NO")