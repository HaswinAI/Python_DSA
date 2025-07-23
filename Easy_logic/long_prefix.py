def long_prefix(strs):
    if not strs:
        return ""

    prefix = strs[0]
    for word in strs[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return "NO LONGER PREFIX"

    return prefix

strs = ["lige","light","liger"]
print(long_prefix(strs))