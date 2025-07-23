def arit_prob(a1,a2,n):
    """nth_term = a1
    d = a2 - a1

    for i in range(1,n):
        nth_term += d
    return nth_term
"""
    return a1 + (n-1) * (a2 - a1)


    
print(arit_prob(2,3,4))