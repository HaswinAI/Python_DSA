n = 91
"""
sum = 0
x = 1
while x <= n:
    sum += x
    x += 1
print(sum)
"""

# print(n*(n+1)//2)

#sum sq od n natural numbers

#print(sum(i**2 for i in range(1,n+1)))

print(n*(n+1)*(2*n+1)//6)