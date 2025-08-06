from collections import Counter

def is_anagram(s,t):
    return Counter(s) == Counter(t)

s = "liosten"
t = "silent"
print(is_anagram(s,t))
