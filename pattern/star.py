n = 5

#increasing triangle

for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

#decreasing triangle
"""
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()
"""
#pyramid
"""
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    for j in range(i):
        print("*",end="")
    for j in range(1,n):
        print(" ",end="")
    print()
"""

#reverse pyramid
"""
for i in range(n):
    for j in range(i+1):
        print("",end=" ")
    for j in range(i,n-1):
        print("*",end="")
    for j in range(i,n):
        print("*",end="")
    print()
"""

#daimond
"""
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    for j in range(i):
        print("*",end="")
    for j in range(1,n):
        print(" ",end="")
    print()

for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n):
        print("*",end="")
    for j in range(i,n-1):
        print("*",end="")
    for j in range(i+1):
        print(" ",end="")
    print()
"""
#decrease new style
"""
n = 10
for i in range(n):
    count = n - i
    print("* " * count)
    """