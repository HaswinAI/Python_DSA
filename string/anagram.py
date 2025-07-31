def is_anagram(s,t):
    return counter(s) == counter(t)

s = "listen"
t = "silent"
print(is_anagram(s,t))
if is_anagram(s,t):
    print(True)
else:
    print(False)