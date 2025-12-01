def romain_en_int(s):
    valeurs = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0
    i = 0

    while i < len(s):
        v1 = valeurs[s[i]]
        if i + 1 < len(s):
            v2 = valeurs[s[i + 1]]
            if v1 < v2:
                total = total + (v2 - v1)
                i = i + 2
            else:
                total = total + v1
                i = i + 1
        else:
            total = total + v1
            i = i + 1
    return total

print(romain_en_int("III"))
print(romain_en_int("LVIII"))
print(romain_en_int("MCMXCIV"))


