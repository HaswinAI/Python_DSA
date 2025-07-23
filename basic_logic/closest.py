def closest(n,m):
    
    #closest 
    q = int(n/m)
    n1 = m*q

    #second use
    if (n*m) > 0:
        n2 = m * (q + 1)
    else:
        n2 = m * (q - 1)


    if (abs(n - n1) > abs(n - n2)):
        print(n2)

    else:
        print(n1)


closest(13,4)