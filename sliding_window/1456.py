#max number of vowels in a substring
def substring(s,k):
    vowel = {"a","e","i","o","u"}
    l,count,result = 0,0,0

    for r in range(len(s)):
        count += 1 if s[r] in vowel else 0
        if r - l + 1 > k:
            count -= 1 if s[l] in vowel else 0
            l += 1
        result = max(count,result)

    return result



s = "abciiidef"
k = 3
print(substring(s,k))