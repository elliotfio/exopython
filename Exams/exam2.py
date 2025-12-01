def score_chaine(s):
    total = 0
    i = 0
    while i < len(s) - 1:
        a = ord(s[i])
        b = ord(s[i + 1])
        diff = a - b
        if diff < 0:
            diff = -diff
        total = total + diff
        i = i + 1
    return total


print(score_chaine("hello"))
print(score_chaine("zaz"))


