arr = [1,1,4,4,3,3,6,6,7]
unique = []
for i in arr:
    if not unique or i != unique[-1]:
        unique.append(i)

print(unique)