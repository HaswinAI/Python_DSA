from collections import Counter

def is_anagram(s,t):
    return Counter(s) == Counter(t)

s = "listen"
t = "silent"
print(is_anagram(s,t))
