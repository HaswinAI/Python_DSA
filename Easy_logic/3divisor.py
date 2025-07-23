def count_divisor(n):
    count = 0
    for i in range(1,n+1):
        if n % 1 == 0:
            count += 1
    return count

def number_with_three(n):
    for i in range(1,n+1):
        if count_divisor(i) == 3:
            print(i,end="")

print(divisor(40))