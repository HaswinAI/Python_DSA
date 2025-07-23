def sum_digit(n):
    sum = 0
    while n != 0:
        last_digit = n % 10
        sum += last_digit
        n //= 10

    return sum

print(sum_digit(12345))
          